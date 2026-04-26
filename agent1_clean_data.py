def run_agent_1(df):
    """Agent 1: validate and clean an uploaded CSV DataFrame.

    Returns a dict with:
      - total_rows: total number of rows
      - missing_values: count of cells with missing data
      - duplicate_rows: number of duplicate rows
      - rows_with_missing: DataFrame of rows that contain at least one null
      - cleaned_data: DataFrame with duplicates removed and nulls filled with empty string
    """
    total_rows = len(df)
    missing_values = int(df.isnull().sum().sum())
    duplicate_rows = int(df.duplicated().sum())

    rows_with_missing = df[df.isnull().any(axis=1)]

    cleaned = df.drop_duplicates()
    # Fill missing values per column type: 0 for numerics, "" for everything else
    for col in cleaned.columns:
        if cleaned[col].dtype.kind in ("i", "u", "f"):
            cleaned[col] = cleaned[col].fillna(0)
        else:
            cleaned[col] = cleaned[col].fillna("")

    return {
        "total_rows": total_rows,
        "missing_values": missing_values,
        "duplicate_rows": duplicate_rows,
        "rows_with_missing": rows_with_missing,
        "cleaned_data": cleaned,
    }