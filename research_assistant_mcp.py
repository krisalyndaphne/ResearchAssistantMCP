import datetime
from base_agent import BaseAgent
from arxiv_search_agent import ArxivSearchAgent
from paper_summarizer_agent import PaperSummarizerAgent
from claim_comparer_agent import ClaimComparerAgent
from citation_formatter_agent import CitationFormatterAgent
from graph_builder_agent import GraphBuilderAgent
from topic_cluster_agent import TopicClusterAgent
from terminology_agent import TerminologyAgent
from timeline_builder_agent import TimelineBuilderAgent
from experiment_extractor_agent import ExperimentExtractorAgent
from report_builder_agent import ReportBuilderAgent

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

        # --- Dynamic Agent Orchestration Example ---
        # This is a simplified example. In a real-world scenario, you would have
        # a more sophisticated query parsing and workflow engine.

        if "fine-tuning methods" in query.lower() or "llm" in query.lower():
            # Workflow for LLM fine-tuning methods comparison

            # 1. ArxivSearchAgent
            arxiv_results = self.agents["arxiv_search_agent"].execute(query)
            output["results"]["ArxivSearchAgent"] = arxiv_results

            # 2. PaperSummarizerAgent (example for first paper if found)
            summarized_papers = []
            if arxiv_results["papers"]:
                for paper in arxiv_results["papers"]:
                    summarized_paper = self.agents["paper_summarizer_agent"].execute(paper["abstract"])
                    summarized_papers.append({"title": paper["title"], **summarized_paper})
                output["results"]["PaperSummarizerAgent"] = summarized_papers

            # 3. ClaimComparerAgent (uses summarized papers)
            if summarized_papers:
                claim_comparison = self.agents["claim_comparer_agent"].execute(summarized_papers)
                output["results"]["ClaimComparerAgent"] = claim_comparison

            # 4. GraphBuilderAgent (uses data from ClaimComparerAgent for accuracy)
            if "ClaimComparerAgent" in output["results"] and output["results"]["ClaimComparerAgent"]["comparison_table"]:
                accuracy_data = {"Accuracy by Method": {}}
                for row in output["results"]["ClaimComparerAgent"]["comparison_table"]:
                    if "Method" in row and "Results" in row:
                        accuracy_data["Accuracy by Method"][row["Method"]] = row["Results"]
                graph_visualization = self.agents["graph_builder_agent"].execute(accuracy_data)
                output["results"]["GraphBuilderAgent"] = graph_visualization

            # 5. TerminologyAgent (uses abstracts from ArxivSearchAgent)
            if arxiv_results["papers"]:
                all_abstracts = " ".join([p["abstract"] for p in arxiv_results["papers"]])
                glossary = self.agents["terminology_agent"].execute(all_abstracts)
                output["results"]["TerminologyAgent"] = glossary

            # 6. ReportBuilderAgent (uses all collected results)
            report = self.agents["report_builder_agent"].execute(output["results"])
            output["results"]["ReportBuilderAgent"] = report

        elif "cite" in query.lower() and "paper" in query.lower():
            # Workflow for citation formatting
            # This would typically involve extracting metadata from the query or a previous agent
            # For this example, we'll use a dummy metadata.
            dummy_metadata = {
                "title": "Example Paper Title",
                "authors": "A. Author, B. Coauthor",
                "year": "2023",
                "source": "Journal of Examples"
            }
            apa_citation = self.agents["citation_formatter_agent"].execute(dummy_metadata, style="APA")
            output["results"]["CitationFormatterAgent_APA"] = apa_citation

        else:
            output["results"]["Message"] = "No specific workflow found for this query. Try 'Compare LLM fine-tuning methods' or 'cite this paper'."

        return output


if __name__ == "__main__":
    assistant = ResearchAssistantMCP()
    assistant.register_agent("arxiv_search_agent", ArxivSearchAgent())
    assistant.register_agent("paper_summarizer_agent", PaperSummarizerAgent())
    assistant.register_agent("claim_comparer_agent", ClaimComparerAgent())
    assistant.register_agent("citation_formatter_agent", CitationFormatterAgent())
    assistant.register_agent("graph_builder_agent", GraphBuilderAgent())
    assistant.register_agent("topic_cluster_agent", TopicClusterAgent())
    assistant.register_agent("terminology_agent", TerminologyAgent())
    assistant.register_agent("timeline_builder_agent", TimelineBuilderAgent())
    assistant.register_agent("experiment_extractor_agent", ExperimentExtractorAgent())
    assistant.register_agent("report_builder_agent", ReportBuilderAgent())

    print("\n--- Running Example 1: LLM Fine-tuning Comparison ---")
    query1 = "Compare LLM fine-tuning methods from 2023–2024"
    sample_output1 = assistant.run_query(query1)
    import json
    print(json.dumps(sample_output1, indent=2))

    print("\n--- Running Example 2: Citation Request ---")
    query2 = "Can you cite an example paper for me?"
    sample_output2 = assistant.run_query(query2)
    print(json.dumps(sample_output2, indent=2))

    print("\n--- Running Example 3: Unrecognized Query ---")
    query3 = "What is the weather like today?"
    sample_output3 = assistant.run_query(query3)
    print(json.dumps(sample_output3, indent=2))


