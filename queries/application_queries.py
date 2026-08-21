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
