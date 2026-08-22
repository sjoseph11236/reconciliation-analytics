from pydantic import BaseModel
from src.scoring import calculate_match_score, MatchScore
from src.artifact_parser import extract_html_text, extract_pdf_text
from llm.resume_job_analyzer import (
    ResumeJobAnalysis,
    analyze_resume_job_match,
)
from repositories.application_repository import (
    get_application_artifacts,
    get_application_analysis,
    save_application_analysis,
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
    
def analyze_application_by_id(
    application_id: int
) -> ApplicationAnalysisResult:
    
    saved_analysis = get_application_analysis(application_id)
    
    if saved_analysis is not None:
        analysis = ResumeJobAnalysis.model_validate_json(
            saved_analysis["analysis_json"]
        )
        
        score = MatchScore(
            required_score=saved_analysis["required_score"],
            nice_to_have_score=saved_analysis["nice_to_have_score"],
            overall_score=saved_analysis["overall_score"],
        )

        return ApplicationAnalysisResult(
            analysis=analysis,
            score=score,
        )
    
    application = get_application_artifacts(application_id)

    if application is None:
        raise ValueError("Application not found")

    result = analyze_application(
        jd_path=application["jd_path"],
        resume_path=application["resume_path"],
    )

    save_application_analysis(
        application_id,
        result,
    )

    return result