def run_agent_1(invoices, pos, payments):

    # Example joins (simplified)
    merged = invoices.merge(pos, on="po_number", how="left")

    # Flag missing PO
    merged["missing_po"] = merged["po_number"].isna()

    # Example tolerance logic
    merged["variance"] = abs(merged["invoice_amount"] - merged["po_amount"]) / merged["po_amount"]
    merged["over_tolerance"] = merged["variance"] > 0.01

    flagged = merged[(merged["missing_po"]) | (merged["over_tolerance"])]

    return {
        "total_invoices": len(invoices),
        "flagged_invoices": len(flagged),
        "flagged_data": flagged
    }