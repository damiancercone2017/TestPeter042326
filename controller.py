from agent1_clean_data import run_agent_1
from agent2_analyze_data import run_agent_2

def main():
    user_input = input("Enter your request: ")

    result_1 = run_agent_1(user_input)
    print("Agent 1 Result:", result_1)

    result_2 = run_agent_2(result_1)
    print("Agent 2 Result:", result_2)

if __name__ == "__main__":
    main()
