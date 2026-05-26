from dotenv import load_dotenv
from graph.workflow import build_graph

load_dotenv()


graph = build_graph()

while True:
    user_input = input("User: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    result = graph.invoke({"user_input": user_input})

    print("Agent:", result["response"])
