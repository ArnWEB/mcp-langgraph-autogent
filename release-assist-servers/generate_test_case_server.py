import os

from langchain_groq import ChatGroq

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("GenerateTestCase")


@mcp.tool()
def generate_testcase(impact_analysis: str) -> str:
    """Generates high-level test cases based on the results of an impact analysis report. this input report can be of plain text or raw string .
    This tool takes an impact analysis report for one or more defects and produces a list of relevant test cases and return response in a raw string format.
    This tool is ideal for QA automation planning, manual testing, and CI/CD test coverage validation."""

    os.environ["GROQ_API_KEY"] = (
        "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"
    )

    # chat_llm,llm = QwenLLM().get_chat_and_base_model()

    llm = ChatGroq(
        model="qwen-qwq-32b",
        temperature=0.0,
        max_retries=2,
        # other params...
    )

    response = llm.invoke(
        f"""Generates high-level test cases based on the impact analysis report.

            \n\n impact_analysis: {impact_analysis}"""
    )

    return response.content


if __name__ == "__main__":
    mcp.run(transport="stdio")
