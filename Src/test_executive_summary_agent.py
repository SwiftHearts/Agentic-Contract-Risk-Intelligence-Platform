from agents.risk_analysis_agent import RiskAnalysisAgent
from agents.negotiation_agent import NegotiationAgent
from agents.executive_summary_agent import ExecutiveSummaryAgent

risk_agent = RiskAnalysisAgent()
negotiation_agent = NegotiationAgent()
summary_agent = ExecutiveSummaryAgent()

question = "What are the highest risks in this contract?"

risk_results = risk_agent.run(question)

negotiation_results = negotiation_agent.run(
    risk_results
)

summary_results = summary_agent.run(
    risk_results,
    negotiation_results
)

print(summary_results)
print(type(summary_results))