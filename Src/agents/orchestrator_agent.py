from agents.risk_analysis_agent import RiskAnalysisAgent
from agents.negotiation_agent import NegotiationAgent
from agents.executive_summary_agent import ExecutiveSummaryAgent


class OrchestratorAgent:
    """
    Coordinates the full contract intelligence workflow.
    """

    def __init__(self):
        self.risk_agent = RiskAnalysisAgent()
        self.negotiation_agent = NegotiationAgent()
        self.summary_agent = ExecutiveSummaryAgent()

        print("Orchestrator Agent initialized")

    def run(self, question):
        """
        Executes the complete agent workflow.
        """

        print("Starting Risk Analysis Agent...")
        risk_results = self.risk_agent.run(question)

        print("Starting Negotiation Agent...")
        negotiation_results = self.negotiation_agent.run(
            risk_results
        )

        print("Starting Executive Summary Agent...")
        summary_results = self.summary_agent.run(
            risk_results,
            negotiation_results
        )

        return summary_results