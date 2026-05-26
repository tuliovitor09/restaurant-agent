from langgraph.graph import StateGraph, END
from graph.state import RestaurantState
from graph.nodes import detect_intent, create_booking, cancel_booking, unknown


def route_intent(state: RestaurantState):
    return state["intent"]


def build_graph():

    builder = StateGraph(RestaurantState)

    builder.add_node(detect_intent, "detect_intent")
    builder.add_node(create_booking, "create_booking")
    builder.add_node(cancel_booking, "cancel_booking")
    builder.add_node(unknown, "unknown")

    builder.set_entry_point("detect_intent")
    builder.add_conditional_edges("detect_intent", route_intent)

    builder.add_edge("create_booking", END)
    builder.add_edge("cancel_booking", END)
    builder.add_edge("unknown", END)

    return builder.compile()
