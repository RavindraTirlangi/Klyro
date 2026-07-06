"""
Klyro startup banner display.
"""

BANNER_ART = r"""
   ____                   _  ____ _     ___
  / ___|___   __ _ _ __ (_)/ ___| |   |_ _|
 | |   / _ \ / _` | '_ \| | |   | |    | |
 | |__| (_) | (_| | | | | | |___| |___ | |
  \____\___/ \__, |_| |_|_|\____|_____|___|
             |___/
"""

TAGLINE = "AI Pair Programming in Your Terminal"


def print_banner(io, version):
    """Print the Klyro startup banner with version info."""
    lines = BANNER_ART.strip("\n").split("\n")
    for line in lines:
        io.tool_output(line)
    io.tool_output(f"  {TAGLINE}")
    io.tool_output(f"  v{version}")
    io.tool_output()
