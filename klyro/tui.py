"""
Textual-based terminal UI for Klyro.

Layout:
  ┌─ Header: Klyro | model | branch ───────────────────┐
  │  ChatView (scrollable Rich markdown output)         │
  ├─────────────────────────────────────────────────────┤
  │  StatusBar: ⣾ Thinking… | tokens sent/recv         │
  ├─────────────────────────────────────────────────────┤
  │  > InputBar (Textual Input widget)                  │
  └─────────────────────────────────────────────────────┘

Only tui.py is changed. io.py / main.py stay completely untouched.
"""

from __future__ import annotations

import re
import threading
from typing import Callable

from rich.markdown import Markdown
from rich.text import Text
from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import ScrollableContainer
from textual.css.query import NoMatches
from textual.reactive import reactive
from textual.widgets import Footer, Header, Input, Label, RichLog, Static

from klyro.io import InputOutput

# ──────────────────────────────────────────────────────────────────────────────
# CSS
# ──────────────────────────────────────────────────────────────────────────────
KLYRO_CSS = """
Screen {
    background: #0b0f14;
}

/* ── Chat area ─────────────────────────────────────────── */
#chat-scroll {
    height: 1fr;
    background: #0b0f14;
}

#chat-log {
    background: #0b0f14;
    color: #d7dce2;
    padding: 0 2;
    scrollbar-color: #334155;
    scrollbar-background: #0b0f14;
}

/* ── Status bar ─────────────────────────────────────────── */
#status-bar {
    height: 1;
    background: #0d1b2a;
    padding: 0 2;
    layout: horizontal;
    border-top: solid #1e2a3a;
}

#status-thinking {
    width: auto;
    color: #38bdf8;
    display: none;
}

#status-thinking.active {
    display: block;
}

#status-tokens {
    width: 1fr;
    content-align: right middle;
    color: #64748b;
    text-align: right;
}

/* ── Input bar ──────────────────────────────────────────── */
#input-bar {
    height: 3;
    background: #0b0f14;
    border-top: solid #1e2a3a;
    padding: 0 1;
    layout: horizontal;
    align: left middle;
}

#input-arrow {
    width: 2;
    color: #0087ff;
    content-align: left middle;
}

#user-input {
    width: 1fr;
    background: #0b0f14;
    color: #d7dce2;
    border: none;
}

#user-input:focus {
    border: none;
    background: #0b0f14;
}

/* ── Header ─────────────────────────────────────────────── */
Header {
    background: #0d1b2a;
    color: #d7dce2;
    border-bottom: solid #1e2a3a;
    height: 1;
}
"""


# ──────────────────────────────────────────────────────────────────────────────
# Textual App
# ──────────────────────────────────────────────────────────────────────────────
class KlyroApp(App):
    """Main Textual TUI for Klyro."""

    CSS = KLYRO_CSS
    TITLE = "Klyro"
    BINDINGS = [
        Binding("ctrl+c", "quit", "Quit", show=False),
        Binding("ctrl+l", "clear_chat", "Clear", show=True),
        Binding("escape", "focus_input", "Focus input", show=False),
    ]

    thinking: reactive[bool] = reactive(False)
    token_info: reactive[str] = reactive("")
    model_name: reactive[str] = reactive("")

    def __init__(self, on_submit: Callable[[str], None], model_name: str = "", **kwargs):
        super().__init__(**kwargs)
        self._on_submit = on_submit
        self.model_name = model_name

    # ── Layout ────────────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        with ScrollableContainer(id="chat-scroll"):
            yield RichLog(
                id="chat-log",
                highlight=True,
                markup=True,
                wrap=True,
                auto_scroll=True,
            )
        with Static(id="status-bar"):
            yield Label("⣾ Thinking…", id="status-thinking")
            yield Label("", id="status-tokens")
        with Static(id="input-bar"):
            yield Label(">", id="input-arrow")
            yield Input(placeholder="Type a message… (Ctrl+C to quit)", id="user-input")
        yield Footer()

    def on_mount(self) -> None:
        self.sub_title = self.model_name
        self.query_one("#user-input", Input).focus()

    # ── Reactive watches ──────────────────────────────────────────────────────

    def watch_thinking(self, value: bool) -> None:
        try:
            lbl = self.query_one("#status-thinking", Label)
            if value:
                lbl.add_class("active")
            else:
                lbl.remove_class("active")
        except NoMatches:
            pass

    def watch_token_info(self, value: str) -> None:
        try:
            self.query_one("#status-tokens", Label).update(value)
        except NoMatches:
            pass

    def watch_model_name(self, value: str) -> None:
        self.sub_title = value

    # ── Input ─────────────────────────────────────────────────────────────────

    @on(Input.Submitted, "#user-input")
    def handle_submit(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        if not text:
            return
        event.input.clear()
        # Echo the user message into the chat log
        log = self.query_one("#chat-log", RichLog)
        log.write(Text("─" * 60, style="#1e3a5f"))
        log.write(Text(f"  {text}", style="#4ade80 bold"))
        # Pass to the IO bridge
        self._on_submit(text)

    # ── Thread-safe API ───────────────────────────────────────────────────────

    def post_message_threadsafe(self, text: str, style: str = "#94a3b8") -> None:
        def _write():
            if text.strip():
                self.query_one("#chat-log", RichLog).write(Text(text, style=style))
        self.call_from_thread(_write)

    def post_markdown_threadsafe(self, markdown: str) -> None:
        def _write():
            self.query_one("#chat-log", RichLog).write(Markdown(markdown, code_theme="monokai"))
        self.call_from_thread(_write)

    def post_separator_threadsafe(self) -> None:
        def _write():
            self.query_one("#chat-log", RichLog).write(Text("─" * 60, style="#1e3a5f"))
        self.call_from_thread(_write)

    def set_thinking_threadsafe(self, active: bool) -> None:
        def _set():
            self.thinking = active
            inp = self.query_one("#user-input", Input)
            inp.disabled = active
            if not active:
                inp.focus()
        self.call_from_thread(_set)

    def set_tokens_threadsafe(self, sent: int, received: int) -> None:
        self.call_from_thread(
            lambda: setattr(self, "token_info", f"↑ {sent:,}  ↓ {received:,}")
        )

    def set_model_threadsafe(self, name: str) -> None:
        self.call_from_thread(lambda: setattr(self, "model_name", name))

    # ── Actions ───────────────────────────────────────────────────────────────

    def action_clear_chat(self) -> None:
        self.query_one("#chat-log", RichLog).clear()

    def action_focus_input(self) -> None:
        self.query_one("#user-input", Input).focus()

    def action_quit(self) -> None:
        self.exit()


# ──────────────────────────────────────────────────────────────────────────────
# IO Bridge
# ──────────────────────────────────────────────────────────────────────────────
class TuiInputOutput(InputOutput):
    """
    Drop-in replacement for InputOutput that routes all output to the
    Textual KlyroApp and reads input from its Input widget.

    main.py already switches to this class when --tui is passed.
    io.py is NOT touched.
    """

    tui_mode = True

    def __init__(self, *args, **kwargs):
        self._app: KlyroApp | None = None
        self._app_thread: threading.Thread | None = None
        self._input_event = threading.Event()
        self._pending_input: str | None = None
        super().__init__(*args, **kwargs)

    # ── App bootstrap ─────────────────────────────────────────────────────────

    def _ensure_app(self, model_name: str = "") -> KlyroApp:
        if self._app is not None:
            return self._app

        import time

        app = KlyroApp(on_submit=self._receive_input, model_name=model_name)
        self._app = app

        t = threading.Thread(target=app.run, daemon=True, name="klyro-tui")
        t.start()
        self._app_thread = t
        time.sleep(0.4)  # Wait for Textual to mount
        return app

    def _receive_input(self, text: str) -> None:
        """Called by KlyroApp when user submits. Unblocks get_input()."""
        self._pending_input = text
        self._input_event.set()

    # ── Output overrides ──────────────────────────────────────────────────────

    def rule(self) -> None:
        if self._app:
            self._app.post_separator_threadsafe()

    def _tool_message(self, message: str = "", strip: bool = True, color=None) -> None:
        self.append_chat_history(
            message.strip() if strip else message,
            linebreak=True,
            blockquote=True,
        )
        if self._app and message.strip():
            style = color if isinstance(color, str) else "#94a3b8"
            self._app.post_message_threadsafe(message, style=style)

    def tool_output(self, *messages, log_only: bool = False, bold: bool = False) -> None:
        if messages:
            hist = " ".join(str(m) for m in messages)
            self.append_chat_history(hist.strip(), linebreak=True, blockquote=True)
            # Parse token counts for the status bar
            if self._app and not log_only and "Tokens:" in hist and "sent" in hist:
                m = re.search(r"(\d+)\s+sent.*?(\d+)\s+received", hist)
                if m:
                    self._app.set_tokens_threadsafe(int(m.group(1)), int(m.group(2)))

        if log_only or not self._app:
            return

        for msg in messages:
            text = msg.plain if isinstance(msg, Text) else str(msg)
            if text.strip():
                style = "bold #d7dce2" if bold else "#94a3b8"
                self._app.post_message_threadsafe(text, style=style)

    def tool_error(self, message: str = "", strip: bool = True) -> None:
        self.num_error_outputs += 1
        self._tool_message(message, strip=strip, color="#f87171")

    def tool_warning(self, message: str = "", strip: bool = True) -> None:
        self._tool_message(message, strip=strip, color="#fb923c")

    def assistant_output(self, message: str, pretty=None) -> None:
        # Hide the thinking spinner
        if self._app:
            self._app.set_thinking_threadsafe(False)

        if not message:
            self.tool_warning("Empty response received from LLM.")
            return

        self.ai_output(message)

        if self._app:
            use_pretty = pretty if pretty is not None else self.pretty
            if use_pretty:
                self._app.post_markdown_threadsafe(message)
            else:
                self._app.post_message_threadsafe(message, style="#d7dce2")

    def llm_started(self) -> None:
        """Show the thinking spinner when the LLM starts."""
        super().llm_started()
        if self._app:
            self._app.set_thinking_threadsafe(True)

    # ── Input override ────────────────────────────────────────────────────────

    def get_input(
        self,
        root,
        rel_fnames,
        addable_rel_fnames,
        commands,
        abs_read_only_fnames=None,
        edit_format=None,
        branch_name=None,
        model_name=None,
    ) -> str:
        app = self._ensure_app(model_name=model_name or "")

        if model_name:
            app.set_model_threadsafe(model_name)

        # Show tracked files in the chat log
        rel_fnames = list(rel_fnames)
        if rel_fnames:
            from klyro.io import get_rel_fname
            rel_ro = [get_rel_fname(f, root) for f in (abs_read_only_fnames or [])]
            files_str = self.format_files_for_input(rel_fnames, rel_ro)
            if files_str.strip():
                app.post_message_threadsafe(files_str.strip(), style="#64748b")

        # Block until user submits
        self._input_event.clear()
        self._pending_input = None
        self._input_event.wait()

        inp = self._pending_input or ""
        self.user_input(inp, log_only=True)
        return inp

    def confirm_ask(
        self,
        question,
        default="y",
        subject=None,
        explicit_yes_required=False,
        group=None,
        allow_never=False,
    ) -> bool:
        self.num_user_asks += 1

        question_id = (question, subject)
        if question_id in self.never_prompts:
            return False
        if group and not group.show_group:
            group = None
        if group:
            allow_never = True

        valid_responses = ["yes", "no", "skip", "all"]
        options = " (Y)es/(N)o"
        if group:
            if not explicit_yes_required:
                options += "/(A)ll"
            options += "/(S)kip all"
        if allow_never:
            options += "/(D)on't ask again"
            valid_responses.append("don't")

        if default.lower().startswith("y"):
            full_q = question + options + " [Yes]: "
        elif default.lower().startswith("n"):
            full_q = question + options + " [No]: "
        else:
            full_q = question + options + f" [{default}]: "

        if subject and self._app:
            self._app.post_message_threadsafe(str(subject), style="bold #d7dce2")

        if self.yes is True:
            res = "n" if explicit_yes_required else "y"
        elif self.yes is False:
            res = "n"
        elif group and group.preference:
            res = group.preference
        else:
            if self._app:
                self._app.post_message_threadsafe(full_q, style="#fb923c")
            while True:
                self._input_event.clear()
                self._pending_input = None
                self._input_event.wait()
                res = (self._pending_input or "").strip().lower()
                if not res:
                    res = default
                    break
                if any(v.startswith(res) for v in valid_responses):
                    break
                if self._app:
                    self._app.post_message_threadsafe(
                        f"Please answer with: {', '.join(valid_responses)}",
                        style="#f87171",
                    )

        res = res.lower()[0] if res else default[0].lower()

        if res == "d" and allow_never:
            self.never_prompts.add(question_id)
            self.append_chat_history(f"{full_q.strip()} {res}", linebreak=True, blockquote=True)
            return False

        is_yes = (res == "y") if explicit_yes_required else res in ("y", "a")

        if group:
            if res == "a" and not explicit_yes_required:
                group.preference = "all"
            elif res == "s":
                group.preference = "skip"

        self.append_chat_history(f"{full_q.strip()} {res}", linebreak=True, blockquote=True)
        return is_yes


# ──────────────────────────────────────────────────────────────────────────────
# Used by main.py (unchanged interface)
# ──────────────────────────────────────────────────────────────────────────────
def should_use_tui(args, return_coder=False):
    if return_coder or not getattr(args, "tui", False):
        return False

    one_shot_attrs = (
        "message",
        "message_file",
        "exit",
        "gui",
        "apply",
        "apply_clipboard_edits",
        "show_repo_map",
        "show_prompts",
        "lint",
        "test",
        "commit",
        "version",
        "list_models",
        "check_update",
        "install_main_branch",
        "upgrade",
        "shell_completions",
    )
    return not any(getattr(args, attr, None) for attr in one_shot_attrs)
