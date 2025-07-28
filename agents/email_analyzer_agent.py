def analyze_email(email_text):
    if "meeting" in email_text.lower():
        return {"status": "meeting_request", "time": "Next Tuesday 3 PM"}
    return {"status": "no_meeting"}
