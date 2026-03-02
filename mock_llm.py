def call_llm(user_input: str) -> dict:
    user_input = user_input.lower()

    if "blocking report" in user_input:
        return {
            "actions": [
                {
                    "action": "check_blocking",
                    "parameters": {
                        "database_name": "SalesDB",
                        "time_window_hours": 2
                    },
                    "execution_policy": {
                        "on_failure": "stop"
                    }
                },
                {
                    "action": "generate_report",
                    "parameters": {
                        "format": "pdf"
                    },
                    "execution_policy": {
                        "on_failure": "stop"
                    }
                }
            ],
            "confidence": 0.91
        }

    elif "blocking" in user_input:
        return {
            "actions": [
                {
                    "action": "check_blocking",
                    "parameters": {
                        "database_name": "SalesDB",
                        "time_window_hours": 2
                    },
                    "execution_policy": {
                        "on_failure": "stop"
                    }
                }
            ],
            "confidence": 0.92
        }

    else:
        return {
            "actions": [
                {
                    "action": "general_response",
                    "parameters": {},
                    "execution_policy": {
                        "on_failure": "continue"
                    }
                }
            ],
            "confidence": 0.60
        }