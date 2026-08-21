from datetime import datetime

# =============================================================================
# TRANSFORM HELPERS
# =============================================================================

def parse_original_date(original_date):
    if not original_date: 
        return None
    
    normalized_date = original_date.replace("\u202f", " ")
    return datetime.strptime(normalized_date, "%a, %b %d, %Y at %I:%M %p")

def extract_annotation(body):
    FORWARDED_MARKERS = [
        "---------- Forwarded message ---------",
        "Forwarded Conversation"
    ]

    for marker in FORWARDED_MARKERS:
        if marker not in body:
            continue

        annotation = body.split(marker, 1)[0].strip()

        if not annotation:
            return None

    return annotation

def normalize_annotation(annotation):
    if annotation is None:
        return None

    normalized = annotation.lower().strip()
    
    if normalized == "rejected":
        return "REJECTED"

    if normalized in ["screening", "phone screening", "phone screening request"]:
        return "SCREENING"

    if normalized == "ai interview":
        return "AI_INTERVIEW"

    if normalized == "coding challenge":
        return "ASSESSMENT"

    if normalized.startswith("assessment] request!"):
        return "ASSESSMENT"

    return None

def classify_email_content(email):
    subject = (email.get("original_subject") or "").lower()
    body = (email.get("body") or "").lower()
    
    body = " ".join(body.split())

    rejection_phrases = [
        "not moving forward with your application",
        "move forward with other candidates",
        "unable to offer you an interview",
    ]

    if any(phrase in body for phrase in rejection_phrases):
        return "REJECTED", "CONTENT_RULE"

    if "application" in subject and "incomplete" in subject:
        return "INCOMPLETE_APPLICATION", "CONTENT_RULE"

    if "right to represent" in subject or "right to represent" in body:
        return "SUBMISSION", "CONTENT_RULE"

    if "referred" in subject:
        return "REFERRED", "CONTENT_RULE"

    return None, None


def filter_emails_by_original_date(emails, start_date, end_date):
    filtered_emails = []

    for email in emails:
        original_date_raw = email.get("original_date_raw")

        if not original_date_raw:
            continue

        parsed_date = parse_original_date(original_date_raw)

        if start_date <= parsed_date <= end_date:
            filtered_emails.append(email)

    return filtered_emails