import json
from openai import AzureOpenAI
import os
from dotenv import load_dotenv


load_dotenv()


class NegotiationAgent:
    """
    The NegotiationAgent accepts structured JSON output from the RiskAnalysisAgent
    and converts identified contract risks into negotiation positions, proposed
    revised language, fallback positions, and business rationale.
    """

    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

        print("Negotiation Agent initialized")

    def run(self, risk_results):
        """
        Accepts the RiskAnalysisAgent output as a Python dictionary
        and returns negotiation recommendations as a Python dictionary.
        """

        if not isinstance(risk_results, dict):
            raise TypeError("risk_results must be a Python dictionary.")

        if "risks" not in risk_results:
            raise ValueError("risk_results must contain a 'risks' key.")

        system_message = """
You are a contract negotiation strategy agent for Sterling Legal Partners.

Your job is to review structured contract risk analysis results and recommend practical negotiation improvements.

You must:
- Use only the risks provided in the input JSON.
- Do not invent new risks.
- Do not invent citations.
- Recommend revised contract language for each risk.
- Explain the negotiation strategy in business-friendly language.
- Prioritize high-severity risks first.
- Return ONLY valid JSON.
- Do not include markdown.
- Do not include commentary outside the JSON.

Return JSON using this exact structure:

{
  "negotiation_overview": "",
  "negotiation_items": [
    {
      "risk_title": "",
      "severity": "",
      "category": "",
      "citation": "",
      "negotiation_position": "",
      "proposed_language": "",
      "fallback_position": "",
      "business_rationale": ""
    }
  ],
  "priority_order": [],
  "recommended_negotiation_strategy": ""
}
"""

        user_message = f"""
Here is the structured risk analysis output from the RiskAnalysisAgent:

{json.dumps(risk_results, indent=2)}

Create negotiation recommendations based only on this input.
"""

        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            
        )

        raw_response = response.choices[0].message.content

        try:
            result = json.loads(raw_response)
        except json.JSONDecodeError as e:
            print("Raw model response was not valid JSON:")
            print(raw_response)
            raise e

        return result