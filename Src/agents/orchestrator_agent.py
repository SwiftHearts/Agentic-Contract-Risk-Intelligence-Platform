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
        try:
            risk_results = self.risk_agent.run(question)
        except Exception as e:
            raise RuntimeError(f"Risk Analysis Agent failed: {e}") from e

        print("Starting Negotiation Agent...")
        try:
            negotiation_results = self.negotiation_agent.run(
                risk_results
            )
        except Exception as e:
            raise RuntimeError(f"Negotiation Agent failed: {e}") from e

        print("Starting Executive Summary Agent...")
        try:
            summary_results = self.summary_agent.run(
                risk_results,
                negotiation_results
            )
        except Exception as e:
            raise RuntimeError(f"Executive Summary Agent failed: {e}") from e

        return {
            "risk_results": risk_results,
            "negotiation_results": negotiation_results,
            "summary_results": summary_results
            }