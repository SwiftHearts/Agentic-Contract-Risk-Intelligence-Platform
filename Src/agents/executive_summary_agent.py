from openai import AzureOpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()


class ExecutiveSummaryAgent:

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

        print("Executive Summary Agent initialized")

    def run(
            self,
            risk_results,
            negotiation_results
        ):

        if not isinstance(risk_results, dict):
                raise TypeError("risk_results must be a dictionary")
 
        if not isinstance(negotiation_results, dict):
                raise TypeError("negotiation_results must be a dictionary")

        system_message = """
                You are an executive contract review agent for Sterling Legal Partners.

                Your job is to review:
                1. Risk Analysis Agent output
                2. Negotiation Agent output

                Prepare an executive-level briefing suitable for a General Counsel, Legal Director, CEO, or Procurement Executive.

                decision_recommendation must be a list of concise executive action items.

                Example:

                "decision_recommendation": [
                    "Do not sign the agreement in its current form",
                    "Require a liability cap",
                    "Require proof of cyber insurance",
                    "Escalate unresolved issues to legal counsel"
]

                Return ONLY valid JSON.

                {
                "executive_summary": "",
                "overall_risk": "",
                "top_risks": [],
                "recommended_actions": [],
                "business_impact": "",
                "decision_recommendation": []
                }
                """

        user_message = f"""
                        Risk Analysis Results:

                        {json.dumps(risk_results, indent=2)}

                        Negotiation Results:

                        {json.dumps(negotiation_results, indent=2)}
                        """

        response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ]
            )

        raw_response = response.choices[0].message.content

        result = json.loads(raw_response)

        return result

           