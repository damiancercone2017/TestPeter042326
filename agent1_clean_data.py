def run_agent_1(user_input):
    cleaned = user_input.strip().lower()
    return {
        "cleaned_text": cleaned,
        "status": "Agent 1 complete"
    }
