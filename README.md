# 🍽️ Restaurant Agent with LangGraph

A simple project for learning **LangGraph + LangChain**, simulating an AI agent capable of:

* Creating restaurant reservations
* Canceling reservations
* Identifying user intent using AI
* Executing different graph nodes based on the detected intent

The main goal of this project is to provide a **hands-on introduction** to graph-based AI workflows using **LangGraph**.

---

# 📚 Concepts Practiced

This project was designed to help practice the following concepts:

* Graph-based workflows
* State management
* Nodes
* Conditional routing
* Intent classification with LLMs
* Service layer
* Separation of responsibilities
* AI provider integration

Architecturally, the flow works like this:

```text
User Input
      ↓
 detect_intent
      ↓
 route_intent
   ↓        ↓
create   cancel
booking  booking
   ↓        ↓
   END     END
```

---

# 🏗️ Project Structure

```text
restaurant-agent/
│
├── app.py
├── .env
│
├── graph/
│   ├── nodes.py
│   ├── state.py
│   └── workflow.py
│
├── prompts/
│   └── classifier.py
│
├── services/
│   └── reservation_service.py
│
└── requirements.txt
```

## Layer Responsibilities

### `app.py`

Application entry point.

Responsible for:

* loading environment variables
* building the graph
* starting the terminal loop
* sending user input to the graph

---

### `graph/state.py`

Defines the shared workflow state.

Example:

```python
from typing import TypedDict, Optional


class RestaurantState(TypedDict):
    user_input: str
    intent: Optional[str]
    response: Optional[str]
```

The state is progressively enriched throughout the workflow.

Example:

Initial state:

```python
{
    "user_input": "I want to reserve a table"
}
```

After `detect_intent`:

```python
{
    "user_input": "I want to reserve a table",
    "intent": "create_booking"
}
```

After `create_booking`:

```python
{
    "user_input": "I want to reserve a table",
    "intent": "create_booking",
    "response": "Booking created"
}
```

---

### `graph/nodes.py`

Contains the workflow nodes.

Each node receives the `RestaurantState` and returns a partial state update.

Example:

```python
return {
    "response": response
}
```

Main nodes:

#### `detect_intent`

Uses an LLM to classify user intent.

Possible outputs:

* `create_booking`
* `cancel_booking`
* `unknown`

#### `create_booking`

Simulates booking creation.

#### `cancel_booking`

Simulates booking cancellation.

#### `unknown`

Fallback node for unknown intents.

---

### `graph/workflow.py`

Responsible for building the LangGraph workflow.

Simplified example:

```python
builder.set_entry_point(
    "detect_intent"
)

builder.add_conditional_edges(
    "detect_intent",
    route_intent
)
```

The `route_intent()` function determines which node will execute next.

---

### `services/reservation_service.py`

Represents the business logic layer.

Currently, it only simulates operations:

```python
Booking created with details: ...
Booking cancelled with details: ...
```

In a real-world scenario, this layer could integrate with:

* databases
* booking APIs
* ERP systems
* CRM systems

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <repo-url>
```

Navigate to the project folder:

```bash
cd restaurant-agent
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\\Scripts\\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install \
langgraph \
langchain-core \
langchain-openai \
python-dotenv
```

---

# 🤖 AI Provider Configuration

The project uses environment variables.

Create a file named:

```text
.env
```

## Example using OpenRouter (free)

```env
OPENAI_API_KEY=your-key
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=deepseek/deepseek-chat-v3-0324:free
```

Create an account:

* [https://openrouter.ai](https://openrouter.ai)

Generate an API key:

* [https://openrouter.ai/keys](https://openrouter.ai/keys)

You can easily switch providers or models.

Examples:

```env
OPENAI_MODEL=google/gemma-3-12b-it:free
```

or

```env
OPENAI_MODEL=mistralai/mistral-small-3.1-24b-instruct:free
```

---

# ▶️ Running the Project

Run:

```bash
python app.py
```

Example:

```text
User: I want to reserve a table for tomorrow at 8 PM
Agent: Booking created with details: I want to reserve a table for tomorrow at 8 PM
```

Cancel booking:

```text
User: I want to cancel my reservation
Agent: Booking cancelled with details: I want to cancel my reservation
```

Exit:

```text
exit
```

or

```text
quit
```

---

# 🔄 How the Workflow Works

## 1. User sends a message

```text
I want to reserve a table
```

## 2. `detect_intent`

The LLM classifies the intent:

```text
create_booking
```

## 3. `route_intent`

Routes execution to:

```text
create_booking
```

## 4. `create_booking`

Executes business logic.

## 5. END

The final result is returned to the user.

---

# 🧠 Important Learnings

During the development of this project, several important Python/AI concepts were practiced.

## Import Side Effects

Avoid initializing heavy objects during module import.

Bad practice:

```python
llm = ChatOpenAI(...)
```

Better:

```python
def get_llm():
    return ChatOpenAI(...)
```

---

## Partial State in LangGraph

Nodes should not return raw values.

Wrong:

```python
return "Booking created"
```

Correct:

```python
return {
    "response": "Booking created"
}
```

---

## Conditional Edges

The router does not execute nodes.

It only tells LangGraph which node should run next.

Example:

```python
return "create_booking"
```

LangGraph executes the node automatically.

---

# 🚀 Suggested Improvements

Ideas to evolve the project:

* extract structured booking information
* validate date and time
* persist bookings in a database
* add conversational memory
* implement booking confirmation before cancellation
* support multiple restaurants
* expose a REST API using FastAPI
* build a web UI
* add observability with LangSmith
* integrate with WhatsApp

---

# 📄 License

This project was created for educational purposes and hands-on learning with LangGraph.
