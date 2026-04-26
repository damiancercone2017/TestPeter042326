def run_agent_2(agent1_result):
    """Agent 2: summarize the validation results produced by Agent 1."""
    total = agent1_result["total_rows"]
    missing = agent1_result["missing_values"]
    dupes = agent1_result["duplicate_rows"]
    cleaned_rows = len(agent1_result["cleaned_data"])

    summary = (
        f"Loaded {total} rows. "
        f"Found {missing} missing value(s) and {dupes} duplicate row(s). "
        f"Cleaned dataset contains {cleaned_rows} row(s)."
    )

    return {
        "summary": summary,
        "status": "Agent 2 complete",
    }