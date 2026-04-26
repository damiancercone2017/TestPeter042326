import pandas as pd
from agent1_clean_data import run_agent_1
from agent2_analyze_data import run_agent_2

def main():
    csv_path = input("Enter the path to your CSV file: ").strip()
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: file '{csv_path}' not found.")
        return
    except pd.errors.ParserError as exc:
        print(f"Error: could not parse CSV file — {exc}")
        return

    result_1 = run_agent_1(df)
    print("Agent 1 Result:")
    print(f"  Total rows    : {result_1['total_rows']}")
    print(f"  Missing values: {result_1['missing_values']}")
    print(f"  Duplicate rows: {result_1['duplicate_rows']}")

    result_2 = run_agent_2(result_1)
    print("Agent 2 Result:", result_2["summary"])

if __name__ == "__main__":
    main()
