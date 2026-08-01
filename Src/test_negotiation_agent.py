from agents.negotiation_agent import NegotiationAgent

agent = NegotiationAgent()

result = agent.run(
    {
        "overall_risk": "High",
        "risks": [
            {
                "title": "Auto Renewal",
                "severity": "High"
            }
        ]
    }
)



print(result)
print(type(result))