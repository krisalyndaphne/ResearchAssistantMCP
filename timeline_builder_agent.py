from base_agent import BaseAgent

class TimelineBuilderAgent(BaseAgent):
    def __init__(self):
        super().__init__("TimelineBuilderAgent")

    def execute(self, paper_metadata):
        # Placeholder for actual timeline building logic
        print(f"TimelineBuilderAgent: Building timeline...")
        if paper_metadata:
            # Simulate a timeline
            return {"timeline": {"2023": ["BERT (key claim)"], "2024": ["GPT-4 (key claim)"]}}
        return {"timeline": {}}


