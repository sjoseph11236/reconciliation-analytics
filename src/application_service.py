from pydantic import BaseModel
from src.scoring import calculate_match_score, MatchScore
from src.artifact_parser import extract_html_text, extract_pdf_text
from llm.resume_job_analyzer import (
    ResumeJobAnalysis,
    analyze_resume_job_match,
)

class ApplicationAnalysisResult(BaseModel):
    analysis: ResumeJobAnalysis
    score: MatchScore

def analyze_application(jd_path: str, resume_path: str) -> ApplicationAnalysisResult:
    job_description_text = extract_html_text(jd_path)
    resume_text = extract_pdf_text(resume_path)
    
    analysis = analyze_resume_job_match(
        resume_text,
        job_description_text
    )
    score = calculate_match_score(analysis=analysis)
    
    return ApplicationAnalysisResult(
        analysis=analysis,
        score=score
    )