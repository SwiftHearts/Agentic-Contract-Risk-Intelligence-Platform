from agents.orchestrator_agent import OrchestratorAgent


def main():

    orchestrator = OrchestratorAgent()

    question = (
        "Identify the highest legal, financial, operational, "
        "and compliance risks in this contract and recommend "
        "appropriate negotiation strategies."
    )

    results = orchestrator.run(question)

    print("\nFINAL RESULTS:")
    print(results)

    print("\nResult type:")
    print(type(results))


if __name__ == "__main__":
    main()