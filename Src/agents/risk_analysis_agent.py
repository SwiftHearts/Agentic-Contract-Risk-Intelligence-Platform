from risk_analysis_agent_core import (
    retrieve_contract_chunks,
    build_context,
    analyze_contract_risk
)


class RiskAnalysisAgent:

    def __init__(self):
        print("Risk Analysis Agent initialized")

    def run(self, question):

        print(f"Analyzing: {question}")

        chunks = retrieve_contract_chunks(question)

        print(f"\nRetrieved {len(chunks)} chunks\n")

        context = build_context(chunks)

        print("Generating risk analysis...\n")

        answer = analyze_contract_risk(
            question,
            chunks
        )

        return answer

        print(answer)

    