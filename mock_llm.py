def call_lm(user_input: str ) -> dict:
    """
    Simulates LLM decision making.
    Return structured JSON-like response.
    """

    user_input = user_input.lower()

    if "blocking" in user_input:
        return{
            "action": "checking_blocking",
            "reason":"User wants blocking analysis",
            "confidence":0.92
        }
    elif "wait" in user_input:
        return{
            "action": "analyze_waits",
            "reason":"User wants wait stats analysis",
            "confidence":0.87
        }
    else:
        return{
            "action": "general_response",
            "reason":"No specific database keyword detected",
            "confidence":0.60
        }