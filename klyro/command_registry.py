"""Explicit slash-command registration.

Keeping command registration separate from implementation prevents helper
methods from becoming user-facing commands merely because of their name.
"""


class CommandSpec:
    def __init__(self, name, method, visible=True, interactive_only=False):
        self.name = name
        self.method = method
        self.visible = visible
        self.interactive_only = interactive_only


def command(name, visible=True, interactive_only=False):
    method = "cmd_" + name.lstrip("/").replace("-", "_")
    return CommandSpec(name, method, visible=visible, interactive_only=interactive_only)


COMMAND_SPECS = (
    command("/add"),
    command("/architect", interactive_only=True),
    command("/ask", interactive_only=True),
    command("/chat-mode", visible=False, interactive_only=True),
    command("/clear"),
    command("/code", interactive_only=True),
    command("/commit"),
    command("/context", interactive_only=True),
    command("/copy"),
    command("/copy-context"),
    command("/diff"),
    command("/drop"),
    command("/editor", visible=False, interactive_only=True),
    command("/editor-model", visible=False, interactive_only=True),
    command("/exit"),
    command("/export"),
    command("/git"),
    command("/help", interactive_only=True),
    command("/image", interactive_only=True),
    command("/lint"),
    command("/load", interactive_only=True),
    command("/ls"),
    command("/map"),
    command("/map-refresh"),
    command("/model", interactive_only=True),
    command("/multiline-mode", visible=False, interactive_only=True),
    command("/ok", visible=False, interactive_only=True),
    command("/paste", interactive_only=True),
    command("/read-only"),
    command("/reasoning-effort"),
    command("/report", interactive_only=True),
    command("/reset"),
    command("/run"),
    command("/save"),
    command("/settings"),
    command("/stats"),
    command("/test"),
    command("/think-tokens"),
    command("/tokens"),
    command("/undo"),
    command("/voice", interactive_only=True),
    command("/weak-model", visible=False, interactive_only=True),
    command("/web"),
)

COMMANDS_BY_NAME = {spec.name: spec for spec in COMMAND_SPECS}
