def run_agent_2(agent1_result):
    text = agent1_result["cleaned_text"]

    summary = f"The cleaned input has {len(text.split())} words."

    return {
        "summary": summary,
        "status": "Agent 2 complete"
    }
