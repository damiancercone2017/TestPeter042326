def run_agent_2(agent1_result):

    total = agent1_result["total_invoices"]
    flagged = agent1_result["flagged_invoices"]

    pct = (flagged / total * 100) if total > 0 else 0

    summary = f"{flagged} out of {total} invoices flagged ({pct:.1f}%)."

    return {
        "summary": summary,
        "status": "Agent 2 complete"
    }