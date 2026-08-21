# Reconciliation Analytics

![Python](https://img.shields.io/badge/Python-3.9-blue)
![SQLite](https://img.shields.io/badge/SQLite-Data%20Store-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-Structured%20Outputs-black)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)

Reconciliation Analytics is an application-intelligence pipeline for reconstructing and analyzing job application history from email events, application artifacts, job descriptions, and resumes.

The current prototype can extract structured application candidates from job-search emails and compare a submitted resume against a job description using evidence-grounded LLM analysis.

## Current Capabilities

- Gmail email-event ingestion and classification
- Structured company and role extraction
- SQLite-backed application reconciliation data
- HTML job-description extraction
- PDF resume extraction
- Structured resume-to-job requirement analysis
- Evidence-backed strong, partial, and missing requirement matches
