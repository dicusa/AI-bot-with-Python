import re

def extract_city_from_query(query: str) -> str:
    """
    Extracts a city name from queries like 'weather in Mumbai' or 'what's the weather in Paris'.
    """
    match = re.search(r'weather (?:in|at|for)?\s*([\w\s]+)', query)
    if match:
        city = match.group(1).strip()
        # Remove trailing words that are not part of the city
        city = re.sub(r'\s+(today|now|please|forecast).*', '', city, flags=re.IGNORECASE)
        return city
    return ""

def extract_topic_from_query(query: str) -> str:
    """
    Extracts a news topic from queries like 'news about technology' or 'show me sports news'.
    """
    match = re.search(r'news (?:about|on|regarding)?\s*([\w\s]+)', query)
    if match:
        topic = match.group(1).strip()
        return topic
    # Fallback: just 'news' means general headlines
    if 'news' in query:
        return ""
    return ""

def parse_email_details(query: str):
    """
    Parses email details from queries like:
    'send email to xyz@example.com subject Hello body How are you'
    Returns (to_email, subject, body)
    """
    email_match = re.search(r'send email to ([\w\.-]+@[\w\.-]+)', query)
    subject_match = re.search(r'subject ([\w\s]+)', query)
    body_match = re.search(r'body (.+)', query)
    to_email = email_match.group(1).strip() if email_match else ""
    subject = subject_match.group(1).strip() if subject_match else "No Subject"
    body = body_match.group(1).strip() if body_match else ""
    return to_email, subject, body

def parse_reminder(query: str):
    """
    Parses reminders from queries like:
    'remind me to call mom in 10 minutes'
    Returns (reminder_text, minutes)
    """
    match = re.search(r'remind me to (.+?) in (\d+) (minute|minutes|hour|hours)', query)
    if match:
        reminder = match.group(1).strip()
        time_value = int(match.group(2))
        unit = match.group(3)
        if 'hour' in unit:
            minutes = time_value * 60
        else:
            minutes = time_value
        return reminder, minutes
    # Fallback: just 'remind me to <task>'
    match = re.search(r'remind me to (.+)', query)
    if match:
        return match.group(1).strip(), 1  # Default 1 minute if no time specified
    return "", 0
