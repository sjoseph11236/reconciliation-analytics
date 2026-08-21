BEGIN TRANSACTION;
-- Remove legacy CSV/Excel-backed application records.
-- email_events.application_id is NULL for all existing rows,
-- so no current email-event relationships are lost.DROP TABLE applications;

DROP TABLE applications;

CREATE TABLE resume_versions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,
    file_path TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE job_descriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company TEXT NOT NULL,
    role TEXT NOT NULL,
    file_path TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id TEXT,

    company TEXT NOT NULL,
    role TEXT NOT NULL,
    submitted_date TIMESTAMP,

    primary_source TEXT,

    resume_version_id INTEGER,
    job_description_id INTEGER,

    notes TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (resume_version_id)
        REFERENCES resume_versions(id),

    FOREIGN KEY (job_description_id)
        REFERENCES job_descriptions(id)
);


CREATE TABLE application_reconciliation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    application_id INTEGER,

    portal_record BOOLEAN,
    legacy_excel_record BOOLEAN,

    confirmation_evidence TEXT,

    reconciliation_status TEXT,
    manual_reconciliation_minutes REAL,
    notes TEXT,

    FOREIGN KEY (application_id)
        REFERENCES applications(id)
);

COMMIT;


