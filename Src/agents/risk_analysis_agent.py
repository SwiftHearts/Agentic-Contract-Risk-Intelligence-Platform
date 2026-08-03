# Import the necessary functions from the risk_analysis_agent_core module
from risk_analysis_agent_core import (
    retrieve_contract_chunks,
    analyze_contract_risk
)

# Define the RiskAnalysisAgent class, which is responsible for analyzing contract risks based on user questions
class RiskAnalysisAgent:

    # Initialize the RiskAnalysisAgent class and print a message indicating that the agent has been initialized
    def __init__(self):
        print("Risk Analysis Agent initialized")

    # Define the run method, which accepts a user's question as input and returns the risk analysis results
    def run(self, question):

        print(f"Analyzing: {question}")

        # Retrieve relevant contract chunks from Azure AI Search based on the user's question
        chunks = retrieve_contract_chunks(question)

        print(f"\nRetrieved {len(chunks)} chunks\n")


        print("Generating risk analysis...\n")

        # Analyze the contract risk based on the user's question and the retrieved contract chunks, returning the analysis results
        answer = analyze_contract_risk(
            question,
            chunks
        )

        return answer

        

    