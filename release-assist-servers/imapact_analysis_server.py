import os

from langchain_groq import ChatGroq

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ImpactAnalysis")


@mcp.tool()
def impact_analysis(defect_descriptions: list[str]) -> str:
    """
    Performs impact analysis on a list of defect descriptions and returns a structured impact analysis report.

    Each report contains:
    - Defect ID
    - Impact Summary
    - User Experience Risk
    - Business Risk

    Example Input:
    [
        "Login page fails to load under poor network conditions.",
        "User receives error 403 when uploading files over 5MB."
    ]

    Example Output:
    - Defect ID: D001
      Impact Summary: ...
      User Experience Risk: ...
      Business Risk: ...
    """

    os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")
    # chat_llm,llm = QwenLLM().get_chat_and_base_model()

    llm = ChatGroq(
        model="qwen-qwq-32b",
        temperature=0.0,
        max_retries=2,
        # other params...
    )
    response = llm.invoke(
        f"""Act as you are a great Impact analyst ,
        Performs impact analysis on a list of defect descriptions and returns a structured impact analysis report.

    Each report contains:
    - Defect ID
    - Impact Summary
    - User Experience Risk
    - Business Risk

    Example Input:
    [
        "Login page fails to load under poor network conditions.",
        "User receives error 403 when uploading files over 5MB."
    ]

    Example Output:
    - Defect ID: D001
      Impact Summary: ...
      User Experience Risk: ...
      Business Risk: ...
        
    \n\n INPUT: \n\n {defect_descriptions}"""
    )
    return response.content


if __name__ == "__main__":
    mcp.run(transport="stdio")
