"""
Opt-in terminal UI support for Klyro.
"""

from collections import deque
from pathlib import Path

from rich.panel import Panel
from rich.text import Text

from klyro.io import InputOutput


class TuiInputOutput(InputOutput):
    """InputOutput variant that keeps a lightweight transcript for TUI prompts."""

    tui_mode = True

    def __init__(self, *args, **kwargs):
        self.transcript = deque(maxlen=200)
        super().__init__(*args, **kwargs)

    def _append_transcript(self, role, message):
        if not message:
            return
        text = message.plain if isinstance(message, Text) else str(message)
        for line in text.splitlines() or [text]:
            self.transcript.append((role, line))

    def _tool_message(self, message="", strip=True, color=None):
        self._append_transcript("tool", message)
        super()._tool_message(message, strip=strip, color=color)

    def tool_output(self, *messages, log_only=False, bold=False):
        if not log_only:
            for message in messages:
                self._append_transcript("tool", message)
        super().tool_output(*messages, log_only=log_only, bold=bold)

    def assistant_output(self, message, pretty=None):
        self._append_transcript("assistant", message)
        super().assistant_output(message, pretty=pretty)

    def user_input(self, inp, log_only=True):
        self._append_transcript("user", inp)
        super().user_input(inp, log_only=log_only)

    def render_tui(self, root, rel_fnames, model_name=None, branch_name=None):
        if not self.pretty:
            return

        try:
            self.console.clear()
        except Exception:
            pass

        cwd = Path(root).resolve()
        title = "Klyro"
        details = []
        if model_name:
            details.append(model_name)
        if branch_name:
            details.append(f"branch {branch_name}")
        details.append(str(cwd))
        header = "  ".join(details)
        self.console.print(Panel(header, title=title, border_style="blue"))

        if rel_fnames:
            files = ", ".join(rel_fnames[:8])
            if len(rel_fnames) > 8:
                files += f", +{len(rel_fnames) - 8} more"
            self.console.print(Text(f"Files: {files}", style="dim"))

        if self.transcript:
            self.console.print()
            for role, line in list(self.transcript)[-20:]:
                style = {
                    "user": "green",
                    "assistant": self.assistant_output_color or "blue",
                    "tool": self.tool_output_color or "white",
                    "error": self.tool_error_color or "red",
                }.get(role, "white")
                label = role[:1].upper()
                self.console.print(Text(f"{label}  {line}", style=style))
            self.console.print()

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
    ):
        self.render_tui(root, rel_fnames, model_name=model_name, branch_name=branch_name)
        return super().get_input(
            root,
            rel_fnames,
            addable_rel_fnames,
            commands,
            abs_read_only_fnames=abs_read_only_fnames,
            edit_format=edit_format,
            branch_name=branch_name,
            model_name=model_name,
        )


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
