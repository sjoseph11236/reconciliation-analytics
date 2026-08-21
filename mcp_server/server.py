from mcp.server import MCPServer

from repositories.application_repository import get_application_artifacts
from src.application_service import (
    ApplicationAnalysisResult,
    analyze_application
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

    application = get_application_artifacts(application_id)

    if application is None:
        raise ValueError(
            f"Application {application_id} not found"
        )

    return analyze_application(
        jd_path=application["jd_path"],
        resume_path=application["resume_path"],
    )

if __name__ == "__main__":
    mcp.run()
    