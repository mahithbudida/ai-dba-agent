from mock_llm import call_lm

def run_agent(user_input: str):
    decision = call_lm(user_input)

    print("\n---Agent Decision---")
    print("Action:",decision["action"])
    print("Reason:",decision["reason"])
    print("Confidence:",decision["confidence"])
    print("--------------------")
    print("\n")


if __name__ =="__main__":
    user_query=input("Enter your database question:")
    run_agent(user_query)

