## langchain-agents

A minimal example project that demonstrates how to build a LangChain agent around Google’s Gemini models and Tavily web search.

The agent uses:

- **`ChatGoogleGenerativeAI`** (Gemini) as the LLM
- **Tavily** as a search backend
- A simple **`search`** tool plus the `TavilySearch` tool wrapper
- LangChain’s **`create_agent`** API to wire the LLM and tools together

---

### Features

- **Gemini-powered agent** via `langchain-google-genai`
- **Web search** using `tavily-python` and `langchain-tavily`
- **Environment-based configuration** with `python-dotenv`
- Simple **CLI entrypoint** in `main.py` that runs a sample query:
  - “Search for top 3 job openings for AI engineering manager in Chennai India!”

---

### Project structure

- `main.py` – creates the LLM, tools, and agent, then runs a sample query.
- `pyproject.toml` – project metadata and dependencies.
- `.env` – environment variables (not committed; see below).

---

### Prerequisites

- **Python** ≥ 3.10
- A **Google API key** for Gemini
- A **Tavily API key** (if you use Tavily’s hosted search)

---

### Installation

```bash
git clone <your-repo-url>
cd langchain-agents

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -e .
```

If you’re not using `pip install -e .`, you can instead run:

```bash
pip install .
```

---

### Environment variables

Create a `.env` file in the project root with at least:

```env
GOOGLE_API_KEY=your_google_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

The app uses `python-dotenv` to load these values automatically.

---

### Usage

```bash
python main.py
```

This will:

1. Load your environment variables.
2. Instantiate a Gemini chat model.
3. Register the Tavily-based search tools.
4. Create a LangChain agent with `create_agent`.
5. Invoke the agent with a hard-coded job search query and print the result.

---

### Customizing the agent

- **Change the model**: Update the `model` parameter in `ChatGoogleGenerativeAI` in `main.py`.
- **Change the query**: Edit the `HumanMessage` content in `main.py`.
- **Add new tools**:
  - Define additional `@tool` functions.
  - Add them to the `tools` list alongside `TavilySearch()`.

---

### Development

This project includes some standard dev tools:

- **black** – code formatter
- **isort** – import sorter

Run them with:

```bash
black .
isort .
```

---

### License

Add your preferred license text here (e.g. MIT, Apache-2.0, proprietary, etc.).
