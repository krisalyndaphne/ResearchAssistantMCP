# ResearchAssistantMCP

This project provides a modular framework for a Research Assistant Multi-Agent Control Plane (MCP). It allows for the integration of various specialized agents to perform research-related tasks.

## Project Structure

- `research_assistant_mcp.py`: Contains the core `ResearchAssistantMCP` class and a `SampleAgent` demonstrating agent integration.
- `base_agent.py`: Defines the `BaseAgent` class, which all custom agents should inherit from.

## Installation

No special installation steps are required beyond a standard Python 3 environment.

## Usage

To run the sample, execute `research_assistant_mcp.py`:

```bash
python3 research_assistant_mcp.py
```

This will output a sample comparison of LLM fine-tuning methods.

## Extending with New Agents

1. Create a new Python file for your agent (e.g., `my_custom_agent.py`).
2. Define your agent class, inheriting from `BaseAgent` and implementing the `execute` method:

   ```python
   from base_agent import BaseAgent

   class MyCustomAgent(BaseAgent):
       def __init__(self):
           super().__init__("MyCustomAgent")

       def execute(self, query):
           # Implement your agent's logic here
           return {"MyCustomAgentResult": f"Processed query: {query}"}
   ```

3. In `research_assistant_mcp.py`, import your new agent and register it with the `ResearchAssistantMCP` instance:

   ```python
   from my_custom_agent import MyCustomAgent
   # ...
   assistant = ResearchAssistantMCP()
   assistant.register_agent("my_custom_agent", MyCustomAgent())
   # ...
   ```

## Sample Output

```json
{
  "query": "Compare LLM fine-tuning methods from 2023–2024",
  "timestamp": "<current_timestamp>",
  "results": {
    "sample_agent": {
      "SampleAgentResult": "This is a sample result from SampleAgent for LLM fine-tuning methods."
    },
    "Accuracy by Method": {
      "LoRA": "88%",
      "Adapters": "82%",
      "Prompt": "71%"
    },
    "Extensibility Ideas": [
      "TopicTrendAgent: track frequency of topics over time",
      "SlideGeneratorAgent: create visual summary slides",
      "AuthorNetworkAgent: graph collaborations between researchers"
    ]
  }
}
```


