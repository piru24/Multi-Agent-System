from crewai import Agent
from config import llm
from tools.input_tool import extract_study_info

class InputAgent(Agent):
    def run(self, input_text):
        return extract_study_info.run(input_text)  # ✅ FIXED

input_agent = InputAgent(
    role="Input Analyzer",
    goal="Extract structured study information",
    backstory="You extract study info using Python tools.",
    llm=llm,
    verbose=True
)