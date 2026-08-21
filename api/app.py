from fastapi import FastAPI, HTTPException

from repositories.application_repository import get_application_artifacts
from src.application_service import (
    ApplicationAnalysisResult,
    analyze_application,
)

app = FastAPI(
    title="Reconciliation Analytics API",
    version="0.1.0"
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get(
    "/applications/{application_id}/analysis",
    response_model=ApplicationAnalysisResult
)
def get_application_analysis(application_id: int):
    
    application = get_application_artifacts(application_id)

    if application is None: 
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )
    return analyze_application(
        jd_path=application["jd_path"],
        resume_path=application["resume_path"]
    )

        