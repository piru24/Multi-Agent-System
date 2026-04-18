from crewai import Agent
from config import llm
from tools.priority_tool import validate_priority
import json

class PriorityAgent(Agent):
    def run(self, study_data):

        prompt = f"""
        You are a study planner.

        Given this data:
        {study_data}

        Rules:
        - Weak subject MUST have highest priority = 3
        - Other subjects = 1 or 2

        Return ONLY a JSON dictionary.
        Do NOT add explanations.
        Do NOT wrap inside another key.

        Example:
        {{"Math": 3, "IT": 1}}
        """

        response = llm.call(prompt).strip()

        # Convert string → dict
        try:
            result = json.loads(response)
        except:
            print("⚠️ JSON parse error")
            return response

        print("DEBUG → Input:", study_data)
        print("DEBUG → Output:", result)
        
        #  Use YOUR tool
        is_valid = validate_priority(result)
        print("Validation:", is_valid)

        return result


priority_agent = PriorityAgent(
    role="Priority Planner",
    goal="Assign priorities",
    backstory="You assign study priorities.",
    llm=llm,
    verbose=True
)