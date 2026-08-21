from pydantic import BaseModel
from llm.resume_job_analyzer import ResumeJobAnalysis

class MatchScore(BaseModel):
    required_score: float
    nice_to_have_score: float
    overall_score: float

MATCH_SCORES = {
    "STRONG_MATCH": 1.0,
    "PARTIAL_MATCH": 0.5,
    "NO_EVIDENCE": 0.0
}


REQUIRED_WEIGHT = 0.90
NICE_TO_HAVE_WEIGHT = 0.10

def calculate_match_score(analysis: ResumeJobAnalysis) -> MatchScore:
    required_scores = []
    nice_to_have_scores = []
    
    for requirement in analysis.requirement_matches:
        score = MATCH_SCORES[requirement.match_status]
        
        if requirement.requirement_type == "REQUIRED":
            required_scores.append(score)
        elif requirement.requirement_type == "NICE_TO_HAVE":
            nice_to_have_scores.append(score)
            
    required_score = sum(required_scores) / len(required_scores)
    nice_to_have_score = (
        sum(nice_to_have_scores) / len(nice_to_have_scores)
        if nice_to_have_scores
        else 0.0 
    )
    
    overall_score = (
        required_score * REQUIRED_WEIGHT + nice_to_have_score * NICE_TO_HAVE_WEIGHT
    )
    
    return MatchScore(
        required_score=required_score,
        nice_to_have_score=nice_to_have_score,
        overall_score=overall_score
    )
