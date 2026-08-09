from agents.risk_analysis_agent import RiskAnalysisAgent
from agents.negotiation_agent import NegotiationAgent

risk_agent = RiskAnalysisAgent()
negotiation_agent = NegotiationAgent()

question = "What are the highest risks in this contract?"

risk_results = risk_agent.run(question)

print("\nRISK RESULTS:")
print(risk_results)

negotiation_results = negotiation_agent.run(risk_results)

print("\nNEGOTIATION RESULTS:")
print(negotiation_results)