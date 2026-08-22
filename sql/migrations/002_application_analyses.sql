CREATE TABLE IF NOT EXISTS application_analyses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    application_id INTEGER NOT NULL UNIQUE,

    required_score REAL NOT NULL,
    nice_to_have_score REAL NOT NULL,
    overall_score REAL NOT NULL,

    analysis_json TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (application_id)
        REFERENCES applications(id)
);