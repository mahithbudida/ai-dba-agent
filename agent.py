from mock_llm import call_llm
from tools import check_blocking, generate_report, general_response
from memory import AgentMemory


def execute_action(step):
    action_name = step["action"]
    params = step.get("parameters", {})

    if action_name == "check_blocking":
        return check_blocking(**params)

    elif action_name == "generate_report":
        return generate_report(**params)

    elif action_name == "general_response":
        return general_response()

    else:
        raise ValueError(f"Unknown action: {action_name}")


def run_agent(user_input: str):
    memory = AgentMemory()
    decision = call_llm(user_input)
    
    print("\n--- Agent Plan ---")
    print(decision)

    for step in decision["actions"]:
        policy = step.get("execution_policy", {})
        on_failure = policy.get("on_failure", "stop")

        try:
            result = execute_action(step)
            memory.store(step["action"],result)
            print("Result:", result)

        except Exception as e:
            print("Error:", e)

            if on_failure == "stop":
                print("Stopping workflow due to failure.")
                break
            elif on_failure == "continue":
                print("Continuing despite failure.")
                continue

    print("\n--- Final Memory State----")
    print(memory.get_all())

if __name__ == "__main__":
    user_query = input("Enter your database request: ")
    run_agent(user_query)