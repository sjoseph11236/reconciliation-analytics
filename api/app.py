from fastapi import FastAPI, HTTPException

from src.application_service import (
    ApplicationAnalysisResult,
    analyze_application_by_id,
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
    try:
        return analyze_application_by_id(application_id)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

        