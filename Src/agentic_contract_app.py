import streamlit as st

from agents.orchestrator_agent import OrchestratorAgent

st.set_page_config(
    page_title="Agentic Contract Intelligence Platform",
    layout="wide"
)

st.title("Agentic Contract Intelligence Platform")

col1, col2 = st.columns([2, 1])


st.markdown("""
    ### Business Value

    - Identifies legal, compliance, and business risks across complex contracts
    - Provides AI-powered negotiation recommendations and prioritizes key issues before signing
    - Delivers executive-ready summaries to support faster, more informed decision-making
    - Reduces manual review effort while improving consistency across contract evaluations
    - Highlights potential financial, operational, and regulatory impacts to reduce business risk
    
    ### Technical Highlights

    - Azure AI Search RAG
    - Azure OpenAI GPT-5-mini
    - Multi-Agent Architecture
    - Agent Orchestration
    - Agent-to-Agent Communication
    - Structured JSON Outputs
    """)

st.info("""
### Workflow

User Question
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Orchestrator Agent
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Risk Analysis Agent
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Negotiation Agent
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Executive Summary Agent
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Recommendation
""")



question = st.text_area(
    "Ask a contract question",
    height=150,
    placeholder="Which contract risks should be negotiated before signing?"
)

show_json = st.checkbox("Show Agent-to-Agent Communication in JSON")

if st.button("Run Agent Workflow"):

    orchestrator = OrchestratorAgent()

    with st.spinner("Running multi-agent workflow..."):
        result = orchestrator.run(question)

    st.success("✅ Workflow Complete")

   

    risk_results = result["risk_results"]
    negotiation_results = result["negotiation_results"]
    summary_results = result["summary_results"]

    # ---------------------------------------------------
    # Executive Summary (Visible to Everyone)
    # ---------------------------------------------------

    st.subheader("📋 Executive Summary Agent")

    st.markdown("### Executive Recommendation")

    recommendations = summary_results.get(
        "decision_recommendation",
        []
    )

    for recommendation in recommendations:
        st.markdown(f"• {recommendation}")

    st.markdown("### Executive Summary")

    st.write(
            summary_results.get(
                "executive_summary",
                "No summary available"
            )
        )

    st.markdown("### Business Impact")

    st.write(
        summary_results.get(
            "business_impact",
            "No business impact available"
        )
    )

    # ---------------------------------------------------
    # Recruiter Technical View
    # ---------------------------------------------------

    

    if show_json:

        st.divider()

        st.subheader("🔍 Risk Analysis Agent")

        st.metric(
            "Overall Risk",
            risk_results.get(
                "overall_risk",
                "Unknown"
            )
        )

        with st.expander(
            "View Risk Analysis Output",
            expanded=True
        ):
            st.json(risk_results)

        st.subheader("🤝 Negotiation Agent")

        with st.expander(
            "View Negotiation Recommendations",
            expanded=True
        ):
            st.json(negotiation_results)

        st.subheader("📋 Executive Summary Agent JSON")

        with st.expander(
            "View Full Executive JSON",
            expanded=True
        ):
            st.json(summary_results)