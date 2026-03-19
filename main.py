from pyexpat import model
from dotenv import load_dotenv
import os

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch

tavily = TavilyClient()

@tool
def search(query: str)-> str:
    """
    Tool which searches the internet 
    Args:
        Query to search
    Returns:
        Search response
    """
    print(f"Querying for {query}")
    return tavily.search(query=query)


llm = ChatGoogleGenerativeAI(
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        model="gemini-2.5-flash"
    )

tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-agents!")
    result = agent.invoke({"messages": HumanMessage(content="Search for top 3 job openings for AI engineering manager in Chennai India!")})
    print(result)

if __name__ == "__main__":
    main()
