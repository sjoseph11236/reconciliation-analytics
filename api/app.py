from src.application_service import (
    ApplicationAnalysisResult,
    analyze_application
)
from fastapi import FastAPI

JD_PATH = (
    "artifacts/job_descriptions/"
    "Software Developer — Alta Fox Capital.html"
)

RESUME_PATH = (
    "artifacts/resumes/"
    "Sayeed J. Software Engineer Resume 1.24.pdf"
)


app = FastAPI(
    title="Reconciliation Analytics API",
    version="0.1.0"
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get(
    "/applications/alta-fox/analysis",
    response_model=ApplicationAnalysisResult
)
def get_alta_fox_analysis():
    return analyze_application(
        jd_path=JD_PATH,
        resume_path=RESUME_PATH
    )