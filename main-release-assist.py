import asyncio
import os

# from utils.qwen_llm_loader import QwenLLM
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient

# from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

# from langchain_core.messages import HumanMessage


# from mcp import ClientSession, StdioServerParameters
# from mcp.client.stdio import stdio_client


# from utils.qwen_llm_loader import QwenLLM

os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")


# chat_llm,llm = QwenLLM().get_chat_and_base_model()


llm = ChatGroq(
    model="qwen-qwq-32b",
    temperature=0.0,
)


async def main():
    client = MultiServerMCPClient(
        {
            "crawl": {
                "command": "python",
                "args": [
                    r"C:\Arnab's Projects\Python\mcp\release-assist-servers\crawl_server.py"
                ],
                "transport": "stdio",
            },
            "impact_analysis": {
                "command": "python",
                "args": [
                    r"C:\Arnab's Projects\Python\mcp\release-assist-servers\imapact_analysis_server.py"
                ],
                "transport": "stdio",
            },
            "generate_testcase": {
                "command": "python",
                "args": [
                    r"C:\Arnab's Projects\Python\mcp\release-assist-servers\generate_test_case_server.py"
                ],
                "transport": "stdio",
            },
        }
    )
    tools = await client.get_tools()
    agent = create_react_agent(llm, tools)
    # Create and run the agent
    agent = create_react_agent(llm, tools)
    agent_response = await agent.ainvoke(
        {
            "messages": r"""Please crawl the following URL: https://chatgpt.com/.

            From the crawled content, extract all relevant software defect descriptions in raw text format.

            Then, perform an impact analysis on each of the defect descriptions and return a structured Impact Analysis Report including:
            - Defect ID
            - Impact Summary
            - User Experience Risk
            - Business Risk

            Finally, based on the Impact Analysis Report, Generates high-level test cases based on the results of an impact analysis report:
            """
        }
    )
    print(agent_response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
