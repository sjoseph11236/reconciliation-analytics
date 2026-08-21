from src.application_service import analyze_application

JD_PATH = (
    "artifacts/job_descriptions/"
    "Software Developer — Alta Fox Capital.html"
)

RESUME_PATH = (
    "artifacts/resumes/"
    "Sayeed J. Software Engineer Resume 1.24.pdf"
)


def main():
    result = analyze_application(
        jd_path=JD_PATH,
        resume_path=RESUME_PATH,
    )
    
    return result.model_dump_json(indent=2) 

if __name__ == "__main__":
    print(main())