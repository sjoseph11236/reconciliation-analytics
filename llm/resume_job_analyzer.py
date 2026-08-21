from typing import Literal
from pydantic import BaseModel
from llm.client import client, OPENAI_MODEL

class RequirementMatch(BaseModel):
    requirement: str
    
    requirement_type: Literal[
        "REQUIRED",
        "NICE_TO_HAVE"
    ]
    
    match_status: Literal[
        "STRONG_MATCH",
        "PARTIAL_MATCH",
        "NO_EVIDENCE"
    ]
    
    # pieces of the JD requirement that the resume demonstrates
    matched_evidence: list[str] 
    # pieces of the JD requirement that the resume does NOT demonstrate
    missing_evidence: list[str] 
    # actual evidence/claims from the resume supporting the match
    resume_evidence: list[str]
    
    explanation: str 
    
class ResumeJobAnalysis(BaseModel):
    requirement_matches: list[RequirementMatch]
    
    strongest_matches: list[str]
    gaps: list[str]
    
    summary: str
    

def analyze_resume_job_match(resume_text: str, job_description_text:str) -> ResumeJobAnalysis:
    prompt = f"""
    Compare the submitted resume against the job description.

    JOB DESCRIPTION

    {job_description_text}

    SUBMITTED RESUME

    {resume_text}
    """
    response = client.responses.parse(
        model=OPENAI_MODEL,
        instructions="""
        You analyze how well a submitted software-engineering resume
        aligns with a specific job description.

        Evaluate the resume only against evidence explicitly contained
        in the provided job description.

        For each meaningful required qualification and relevant
        nice-to-have:

        - Identify the requirement.
        - Determine whether the resume provides a STRONG_MATCH,
        PARTIAL_MATCH, or NO_EVIDENCE.
        - Provide the specific resume evidence supporting the assessment.
        - Briefly explain the reasoning.

        Rules:
        - Use only information contained in the submitted resume.
        - Do not assume experience that is not explicitly represented.
        - Do not use outside knowledge about the candidate.
        - Do not invent resume evidence.
        - NO_EVIDENCE must have an empty resume_evidence list.
        - PARTIAL_MATCH means related evidence exists but does not fully
        demonstrate the requirement.
        - STRONG_MATCH requires direct, substantive evidence.
        - Evaluate nice-to-have requirements separately rather than
        treating their absence as equivalent to missing a required skill.
        - matched_evidence should identify the specific parts of a requirement
        that are explicitly supported by the resume.
        - missing_evidence should identify the specific parts of a requirement
        for which the resume provides no explicit evidence.
        - Do not put something in missing_evidence merely because the wording
        differs; judge whether the resume provides substantive evidence.
        - Classify each requirement as REQUIRED or NICE_TO_HAVE based only
  on how the job description categorizes it.
        """,
        input=prompt,
        text_format=ResumeJobAnalysis,
    )
    
    return response.output_parsed

