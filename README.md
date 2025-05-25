# MCP Test

MCP Test is a Python-based project that leverages advanced AI models and tools to perform tasks such as mathematical computations, impact analysis, test case generation, and more. The project integrates with Groq's AI models and provides a modular architecture for building intelligent agents and tools.

## Features

- **Mathematical Computations**: Perform basic arithmetic operations using the `math_server`.
- **Impact Analysis**: Analyze defect descriptions and generate structured impact reports.
- **Test Case Generation**: Automatically generate high-level test cases based on impact analysis reports.
- **Web Crawling**: Extract defect descriptions from web pages.
- **Weather Information**: Retrieve weather details for a given location.
- **Integration with Groq AI Models**: Utilize Groq's `qwen-qwq-32b` model for advanced AI capabilities.
- **Modular Architecture**: Easily extend the project by adding new tools and servers.

## Project Structure

```
.
├── main-autogen-math.py         # Main script for math-related tasks
├── main-langgraph_react.py      # Main script for LangGraph React agent
├── main-langgraph_states.py     # Main script for LangGraph state-based agent
├── main-release-assist.py       # Main script for release assistance
├── release-assist-servers/      # Servers for release assistance tools
│   ├── crawl_server.py          # Server for web crawling
│   ├── generate_test_case_server.py # Server for test case generation
│   ├── imapact_analysis_server.py   # Server for impact analysis
├── servers/                     # General-purpose servers
│   ├── math_server.py           # Server for math operations
│   ├── weather_server.py        # Server for weather information
├── utils/                       # Utility scripts
│   ├── async_wrapper.py         # Async wrapper for chat models
│   ├── huggingfacellm_local.py  # Local HuggingFace model loader
│   ├── qwen_llm_loader.py       # Loader for Qwen LLM
├── pyproject.toml               # Project dependencies and metadata
├── .python-version              # Python version used in the project
├── .gitignore                   # Git ignore file
└── README.md                    # Project documentation
```

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/mcp-test.git
   cd mcp-test
   ```
test
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Ensure you have Python 3.12 installed (as specified in `.python-version`).

4. Set up environment variables:
   Create a `.env` file and add your Groq API key:
   ```
   GROQ_API_KEY=<TOKEN>
   ```

## Usage


### Running the LangGraph React Agent
To run the LangGraph React agent:
```sh
python main-langgraph_react.py
```

### Running the LangGraph State-Based Agent
To run the LangGraph state-based agent:
```sh
python main-langgraph_states.py
```


### Running the LangGraph React Agent for release asist client
To run the LangGraph state-based agent:
```sh
python main-release-assist.py
```

## Adding New Tools or Servers

1. Create a new server in the `servers/` or `release-assist-servers/` directory.
2. Use the `FastMCP` class to define tools.
3. Register the server in the appropriate main script.

## Dependencies

The project uses the following key dependencies:
- [LangChain](https://github.com/hwchase17/langchain)
- [Groq](https://groq.com/)
- [HuggingFace Transformers](https://huggingface.co/transformers/)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)

For a full list of dependencies, see the `pyproject.toml` file.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

- Groq for providing the `qwen-qwq-32b` model.
- LangChain for the powerful framework for building AI tools.
- HuggingFace for the model loading and pipeline utilities.


