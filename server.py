from mcp.server.fastmcp import FastMCP

mcp = FastMCP("EMRIX AI YouTube Automation")

@mcp.tool()
def emrix_project_status() -> str:
    """Return information about the EMRIX AI YouTube automation project."""
    return (
        "Project: EMRIX AI YouTube Automation\n"
        "Target audience: USA\n"
        "Narration: American English\n"
        "Format: 50-60 second YouTube Shorts\n"
        "Goal: Automate scripts, narration, captions, visuals, and rendering.\n"
        "Note: This server does not yet access the phone's Termux files "
        "or upload videos to YouTube."
    )

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
