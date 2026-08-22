GET_APPLICATION_ARTIFACTS = """
SELECT
    a.id,
    a.company,
    a.role,
    rv.file_path AS resume_path,
    jd.file_path AS jd_path
FROM applications a
JOIN resume_versions rv
    ON a.resume_version_id = rv.id
JOIN job_descriptions jd
    ON a.job_description_id = jd.id
WHERE a.id = ?
"""

GET_APPLICATION_ANALYSIS = """
SELECT
    application_id,
    required_score,
    nice_to_have_score,
    overall_score,
    analysis_json
FROM application_analyses
WHERE application_id = ?
"""



INSERT_APPLICATION_ANALYSIS = """
INSERT INTO application_analyses (
    application_id,
    required_score,
    nice_to_have_score,
    overall_score,
    analysis_json
) 
VALUES(?,?,?,?,?);
"""

