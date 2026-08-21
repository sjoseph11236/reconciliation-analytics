import base64
# =============================================================================
# GMAIL HELPERS
# =============================================================================

def get_forwarded_field(lines, field_name):
    FORWARDED_HEADERS = ["From", "Date", "Subject", "To"]
    
    field_prefix = f"{field_name}:"
    
    for index, line in enumerate(lines):
        if line.startswith(field_prefix):
            value = line.split(":", 1)[1].strip()
        
            for next_line in lines[index + 1:]:
                if any(
                    next_line.startswith(f"{header}:")
                    for header in FORWARDED_HEADERS
                ):
                    break
                if next_line == "":
                    break
                value += " " + next_line.strip()
                
            return value
    
    return None

def find_plain_text(part): 
    if part["mimeType"] == "text/plain":
        encoded_data = part["body"]["data"]
        decoded_bytes = base64.urlsafe_b64decode(encoded_data)
        return decoded_bytes.decode("utf-8")
    
    for child in part.get("parts", []):
        body_text  = find_plain_text(child)
        
        if body_text is not None:
            return body_text 
    
    return None

def get_plain_text_body(message):
    return find_plain_text(message["payload"])

