import asyncio
import os

from dotenv import load_dotenv
# from utils.qwen_llm_loader import QwenLLM
from langchain_groq import ChatGroq
# from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
# from utils.qwen_llm_loader import QwenLLM

load_dotenv()

# from langchain_core.messages import HumanMessage





os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")


#hugging face pipeline async not supported by langchain_groq for mcp client

# chat_llm,llm = QwenLLM().get_chat_and_base_model()


# llm = ChatGroq(
#     model="qwen-qwq-32b",
#     temperature=0.0,
#     max_retries=2,
#     # other params...
# )

inference_server_url = "http://localhost:8000/v1"

llm = ChatOpenAI(
    model="Qwen/Qwen2.5-0.5B-Instruct",
    openai_api_key="EMPTY",
    openai_api_base=inference_server_url,
    max_tokens=100,
    temperature=0,
)


async def main():
    studio_server = StdioServerParameters(
        command="python", args=[r"C:\Arnab's Projects\Python\mcp\servers\math_server.py"]
    )
    async with stdio_client(studio_server) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(llm, tools)
            agent_response = await agent.ainvoke({"messages": "Test two numbers 1 and 2"})
            print(agent_response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())


# server_params = StdioServerParameters(
#     command="python",
#     # Make sure to update to the full absolute path to your math_server.py file
#     args=["/path/to/math_server.py"],
# )

# async with stdio_client(server_params) as (read, write):
#     async with ClientSession(read, write) as session:
#         # Initialize the connection
#         await session.initialize()

#         # Get tools
#         tools = await load_mcp_tools(session)

#         # Create and run the agent
#         agent = create_react_agent("openai:gpt-4.1", tools)
#         agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
