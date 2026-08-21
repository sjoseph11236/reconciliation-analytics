APPLICATION_ARTIFACTS = {
    1: {
        "company": "Alta Fox Capital",
        "role": "Software Developer",
        "jd_path": (
            "artifacts/job_descriptions/"
            "Software Developer — Alta Fox Capital.html"
        ),
        "resume_path": (
            "artifacts/resumes/"
            "Sayeed J. Software Engineer Resume 1.24.pdf"
        ),
    }
}


def get_application_artifacts(application_id: int):
    return APPLICATION_ARTIFACTS.get(application_id)