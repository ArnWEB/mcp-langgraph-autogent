import asyncio
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()

# from utils.qwen_llm_loader import QwenLLM


# from langchain.chat_models import init_chat_model
# model = init_chat_model("openai:gpt-4.1")


os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")

llm = ChatGroq(
    model="qwen-qwq-32b",
    temperature=0.0,
    max_retries=2,
    # other params...
)


inference_server_url = "http://localhost:8000/v1"

llm = ChatOpenAI(
    model="/app/model",
    openai_api_key="EMPTY",
    openai_api_base=inference_server_url,
    max_tokens=100,
    temperature=0,
)

# chat_llm,llm = QwenLLM().get_chat_and_base_model()

# print(chat_llm.invoke("What is pluto?"))



async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": [r"C:\Arnab's Projects\Python\mcp\servers\math_server.py"],
                "transport": "stdio",
            }
        }
    )
    tools = await client.get_tools()

    def call_model(state: MessagesState):
        response = llm.bind_tools(tools).invoke(state["messages"])
        return {"messages": response}

    builder = StateGraph(MessagesState)
    builder.add_node(call_model)
    builder.add_node(ToolNode(tools))
    builder.add_edge(START, "call_model")
    builder.add_conditional_edges(
        "call_model",
        tools_condition,
    )
    builder.add_edge("tools", "call_model")
    graph = builder.compile()
    math_response = await graph.ainvoke({"messages": "Add two number 5,7"})
    # weather_response = await graph.ainvoke({"messages": "what is the weather in nyc?"})
    print(math_response["messages"][-1].content)



if __name__ == "__main__":
    asyncio.run(main())
