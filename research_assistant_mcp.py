import datetime
from base_agent import BaseAgent

class SampleAgent(BaseAgent):
    def __init__(self):
        super().__init__("SampleAgent")

    def execute(self, query):
        if "LLM fine-tuning methods" in query:
            return {"SampleAgentResult": "This is a sample result from SampleAgent for LLM fine-tuning methods."}
        return {"SampleAgentResult": "No relevant data for this query from SampleAgent."}

class ResearchAssistantMCP:
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent_name, agent_instance):
        if not isinstance(agent_instance, BaseAgent):
            raise ValueError("Agent instance must inherit from BaseAgent")
        self.agents[agent_name] = agent_instance

    def run_query(self, query):
        print(f"Running query: {query}")
        results = self._execute_agents(query)
        return results

    def _execute_agents(self, query):
        print("Executing registered agents...")
        output = {
            "query": query,
            "timestamp": datetime.datetime.now().isoformat(),
            "results": {}
        }

        for agent_name, agent_instance in self.agents.items():
            agent_result = agent_instance.execute(query)
            output["results"][agent_name] = agent_result

        # Original sample output logic (can be replaced by dedicated agents)
        if "LLM fine-tuning methods" in query:
            output["results"]["Accuracy by Method"] = {
                "LoRA": "88%",
                "Adapters": "82%",
                "Prompt": "71%"
            }
            output["results"]["Extensibility Ideas"] = [
                "TopicTrendAgent: track frequency of topics over time",
                "SlideGeneratorAgent: create visual summary slides",
                "AuthorNetworkAgent: graph collaborations between researchers"
            ]
        return output


if __name__ == "__main__":
    assistant = ResearchAssistantMCP()
    assistant.register_agent("sample_agent", SampleAgent())

    query = "Compare LLM fine-tuning methods from 2023–2024"
    sample_output = assistant.run_query(query)
    print("\nSample Output:")
    import json
    print(json.dumps(sample_output, indent=2))


