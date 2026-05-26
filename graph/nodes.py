import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from graph.state import RestaurantState
from prompts.classifier import SYSTEM_PROMPT
from services.reservation_service import ReservationService


def get_llm():
    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0,
    )


reservation_service = ReservationService()


def detect_intent(state: RestaurantState):
    user_input = state["user_input"]

    llm = get_llm()
    response = llm.invoke(
        [SystemMessage(content=SYSTEM_PROMPT), HumanMessage(content=user_input)]
    )

    intent = response.content.strip()

    return {"intent": intent}


def create_booking(state: RestaurantState):

    response = reservation_service.create_booking(state["user_input"])

    return {"response": response}


def cancel_booking(state: RestaurantState):
    response = reservation_service.cancel_booking(state["user_input"])

    return {"response": response}


def unknown(state: RestaurantState):
    return {"response": "Sorry, I didn't understand your request."}
