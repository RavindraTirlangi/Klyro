"""
Klyro startup banner display.
"""

BANNER_ART = r"""
[#4C4CFF]   #    #   [/#4C4CFF][#6666FF] #      [/#6666FF][#7F7FFF] #   #   [/#7F7FFF][#9999FF] ######  [/#9999FF][#B2B2FF]  ####   [/#B2B2FF]
[#4C4CFF]   #   #    [/#4C4CFF][#6666FF] #      [/#6666FF][#7F7FFF]  # #    [/#7F7FFF][#9999FF] #     # [/#9999FF][#B2B2FF] #    #  [/#B2B2FF]
[#4C4CFF]   ####     [/#4C4CFF][#6666FF] #      [/#6666FF][#7F7FFF]   #     [/#7F7FFF][#9999FF] ######  [/#9999FF][#B2B2FF] #    #  [/#B2B2FF]  [bold white]Klyro CLI v{__version__}[/bold white]
[#4C4CFF]   #   #    [/#4C4CFF][#6666FF] #      [/#6666FF][#7F7FFF]   #     [/#7F7FFF][#9999FF] #   #   [/#9999FF][#B2B2FF] #    #  [/#B2B2FF]
[#4C4CFF]   #    #   [/#4C4CFF][#6666FF] ###### [/#6666FF][#7F7FFF]   #     [/#7F7FFF][#9999FF] #    #  [/#9999FF][#B2B2FF]  ####   [/#B2B2FF]

[#808080]------------------------------------------------------[/#808080]
"""

def print_banner(io, version):
    """Print the Klyro startup banner with version info."""
    logo = BANNER_ART.replace("{__version__}", version)
    lines = logo.strip("\n").split("\n")
    for line in lines:
        if hasattr(io, "console") and io.console:
            io.console.print(line)
        else:
            io.tool_output(line)

