from mcp.server import MCPServer

from src.application_service import (
    ApplicationAnalysisResult,
    analyze_application_by_id
)

mcp = MCPServer("Reconciliation Analytics")


@mcp.tool()
def health() -> str:
    """
    Check whether the Reconciliation Analytics MCP server is running.

    Returns:
        str: status of ok
    """
    
    return "ok"


@mcp.tool()
def analyze_job_application(
    application_id: int
) -> ApplicationAnalysisResult:
    """Analyze the resume-to-job match for a reconciled job application."""
    return analyze_application_by_id(application_id)
 

if __name__ == "__main__":
    mcp.run()
    