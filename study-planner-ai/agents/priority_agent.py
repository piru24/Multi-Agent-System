from crewai import Agent
from config import llm
from tools.priority_tool import validate_priority
import json
import re

class PriorityAgent(Agent):
    def run(self, study_data):

        prompt = f"""
        You are an intelligent study planning assistant.

        Your task is to assign priority levels to subjects.

        Input:
        {study_data}

        Rules:
        - Weak subject MUST have highest priority = 3
        - Exactly ONE subject must have priority = 3
        - Other subjects must have priority = 1 or 2
        - Do NOT assign multiple 3s

        Constraints:
        - Output must be a valid JSON dictionary
        - Do NOT include explanations
        - Do NOT include extra text
        - Return JSON only

        Example:
        {{"Math": 3, "IT": 1}}
        """

        response = llm.call(prompt).strip()

        # extract JSON part only
        match = re.search(r'\{.*\}', response, re.DOTALL)

        if match:
            json_str = match.group()
            try:
                result = json.loads(json_str)
            except:
                print("JSON parse error")
                return response
        else:
            print("No JSON found")
            return response

        # DEBUG logs
        print("DEBUG → Input:", study_data)
        print("DEBUG → Output:", result)

        # validation
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