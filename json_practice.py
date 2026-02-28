import json

""""
Wait_Summary = {'total_waits': 3, 'High': 1, 'Medium': 1, 'Low': 1}

json_output=json.dumps(Wait_Summary,indent=4)

print("JSON Format:")
print(json_output)

parsed=json.loads(json_output)

print("\nBack to Python dick:")
print("High waits:",parsed["High"])

result=Wait_Summary["High"]
print("High:",result)

"""

fake_api_response = {
    "analysis":{
        "risk_level": "HIGH",
        "recommendation": "Create non-clusterd index on OrderDate",
        "estimated_improvement":"35%"
    }    

}

fake_api_response_string = """
{
    "analysis": {
        "risk_level": "HIGH",
        "recommendation": "Create non-clusterd index on OrderDate",
        "estimated_improvement": "35%",
        "confidence_score": 0.87
    }    
}
"""


data=json.loads(fake_api_response_string)
#data=fake_api_response

score=data["analysis"]["confidence_score"]
ConfidenceScore= score * 100

print("\nRisk Level:",data["analysis"]["risk_level"])
print("Recommendation:",data["analysis"]["recommendation"])
print(f"ConfidenceScore:{round(ConfidenceScore,2)}%")
print("\n")
