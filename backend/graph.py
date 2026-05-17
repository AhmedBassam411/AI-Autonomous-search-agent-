from langgraph.graph import StateGraph, END

from backend.agents import (
    research_coordinator,
    content_analyzer,
    synthesis_agent
)


def build_graph():

    workflow = StateGraph(dict)

    # -----------------------------
    # PLAN NODE
    # -----------------------------
    def plan_node(state):

        state["plan"] = research_coordinator(
            state["input"]
        )

        return state

    # -----------------------------
    # ANALYSIS NODE
    # -----------------------------
    def analyze_node(state):

        state["analysis"] = content_analyzer(
            state["plan"]
        )

        return state

    # -----------------------------
    # SYNTHESIS NODE
    # -----------------------------
    def synth_node(state):

        combined_text = f"""

PLAN:
{state.get("plan")}

ANALYSIS:
{state.get("analysis")}

"""

        state["report"] = synthesis_agent(
            combined_text
        )

        return state

    workflow.add_node("plan", plan_node)
    workflow.add_node("analyze", analyze_node)
    workflow.add_node("synthesize", synth_node)

    workflow.set_entry_point("plan")

    workflow.add_edge("plan", "analyze")
    workflow.add_edge("analyze", "synthesize")
    workflow.add_edge("synthesize", END)

    return workflow.compile()