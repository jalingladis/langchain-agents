# langchain-agents

Minimal LangChain agent examples focused on tool calling with a custom agent loop.

This project demonstrates a practical `.bind_tools` workflow where the model:

- fetches product prices from a catalog tool
- applies tier-based discounts through a second tool
- follows strict system rules to avoid guessing values

## What this project does

The current `main.py` runs a shopping-assistant style agent that:

- uses `init_chat_model(...)` and binds tools with `llm.bind_tools(tools)`
- executes a manual iteration loop (`MAX_ITERATIONS`) to process tool calls
- enforces one tool call per iteration
- appends `ToolMessage` responses back into conversation state
- returns a final answer once no further tool calls are requested

## Tools implemented

- `get_product_price(product: str) -> float`
  - Looks up a product in an in-memory catalog:
    - `laptop`: `1299.99`
    - `headphones`: `149.95`
    - `keyboard`: `89.50`
- `apply_discount(price: float, discount_tier: str) -> float`
  - Applies one of:
    - `bronze`: `5%`
    - `silver`: `12%`
    - `gold`: `23%`

## Prerequisites

- Python `>=3.10`
- A Google Generative AI API key

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Environment variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

## Run

```bash
python main.py
```

Default prompt in code:

`What is the price of a laptop after applying a gold discount?`

## Notes on agent behavior

The system prompt contains strict rules:

1. Never guess a product price.
2. Call `get_product_price` first.
3. Call `apply_discount` only after a real price is returned.
4. Never compute discount math directly in the model response.
5. Ask for discount tier if missing.

This makes the example useful for learning reliable multi-step tool usage.

## Key dependencies

- `langchain`
- `langchain-google-genai`
- `python-dotenv`
- `langsmith`

See `pyproject.toml` for the full dependency list.
