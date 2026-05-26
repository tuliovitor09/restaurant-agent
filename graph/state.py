from typing import TypedDict, Optional


class RestaurantState(TypedDict):
    user_input: str
    intent: Optional[str]
    response: Optional[str]
