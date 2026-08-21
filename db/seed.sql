INSERT INTO resume_versions (
    name,
    file_path
) VALUES (
    'Sayeed J. Software Engineer Resume 1.24',
    'artifacts/resumes/Sayeed J. Software Engineer Resume 1.24.pdf'
);

INSERT INTO job_descriptions (
    company,
    role,
    file_path
) VALUES (
    'Alta Fox Capital',
    'Software Developer',
    'artifacts/job_descriptions/Software Developer — Alta Fox Capital.html'
);

INSERT INTO applications (
    company,
    role,
    resume_version_id,
    job_description_id
)
VALUES (
    'Alta Fox Capital',
    'Software Developer',
    1,
    1
);