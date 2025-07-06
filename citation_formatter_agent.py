from base_agent import BaseAgent

class CitationFormatterAgent(BaseAgent):
    def __init__(self):
        super().__init__("CitationFormatterAgent")

    def execute(self, metadata, style="APA"):
        # Placeholder for actual citation formatting logic
        print(f"CitationFormatterAgent: Formatting citation in {style} style...")
        title = metadata.get("title", "N/A")
        authors = metadata.get("authors", "N/A")
        year = metadata.get("year", "N/A")
        source = metadata.get("source", "N/A")

        if style == "APA":
            return f"{authors} ({year}). {title}. {source}."
        elif style == "IEEE":
            return f"[{authors}], \"{title},\" {source}, {year}."
        else:
            return f"Unsupported citation style: {style}"


