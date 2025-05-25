import asyncio
# from pathlib import Path
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, mcp_server_tools
from autogen_agentchat.agents import AssistantAgent
from autogen_core import CancellationToken
from autogen_agentchat.ui import Console
# from autogen_ext.tools.mcp import SseMcpToolAdapter, SseServerParams
# import os
from dotenv import load_dotenv
from autogen_core.models import ModelFamily
import os


# Get environment variables
load_dotenv()


## GLOBAL SETTINGS
BASE_URL = "https://api.groq.com/openai/v1"
MODEL_NAME = "qwen-qwq-32b"
API_KEY = os.environ.get("GROQ_API_KEY")

# Initialize the model client
model_client = OpenAIChatCompletionClient(
    model=MODEL_NAME,
    base_url=BASE_URL,
    api_key=API_KEY,
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": False,
        "family": ModelFamily.ANY,
    },
)


async def main() -> None:

    # Setup server params for local filesystem access
    math_server = StdioServerParams(
        command="python", args=[r"C:\Arnab's Projects\Python\mcp\servers\math_server.py"]
    )
    math_tools = await mcp_server_tools(math_server)


    # Combine the tools from both servers into a single list
    all_tools = math_tools

    # Create an agent that can use the fetch tool.
    # model_client = OpenAIChatCompletionClient(model="qwen-qwq-32b", api_key="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")
    agent = AssistantAgent(
        name="demo_agent",
        model_client=model_client,
        tools=all_tools,
        reflect_on_tool_use=True,
        system_message=(
            "You are an intelligent assistant with access to tools such as 'adapter', "
        ),
    )
    await Console(
        agent.run_stream(
            task="what's (3 + 5) x 12?", cancellation_token=CancellationToken()
        )
    )


if __name__ == "__main__":
    asyncio.run(main())