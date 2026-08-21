CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id TEXT,

    company TEXT NOT NULL,
    role TEXT NOT NULL,
    submitted_date TIMESTAMP,

    primary_source TEXT,
    resume_version_id INTEGER,

    notes TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS email_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gmail_id TEXT UNIQUE NOT NULL,
    application_id INTEGER,  

    original_from TEXT NOT NULL,
    original_to TEXT NOT NULL,
    original_subject TEXT NOT NULL,

    original_date TIMESTAMP NOT NULL,
    original_date_raw TEXT NOT NULL,
    
    body TEXT NOT NULL,

    raw_annotation TEXT,
    event_type TEXT,
    signal_source TEXT

    FOREIGN KEY (application_id)
        REFERENCES applications(id)
);


-- reconciliation / ETL

CREATE TABLE IF NOT EXISTS application_candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email_event_id INTEGER NOT NULL UNIQUE,

    company TEXT,
    role TEXT,

    company_source TEXT NOT NULL,
    role_source TEXT NOT NULL,

    confidence REAL NOT NULL,

    FOREIGN KEY(email_event_id)
        REFERENCES email_events(id)
);


CREATE TABLE IF NOT EXISTS application_reconciliation (
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

