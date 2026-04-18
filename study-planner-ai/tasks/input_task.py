from crewai import Task
from agents.input_agent import input_agent

def create_input_task(user_input):
    return Task(
        description=f"""
        Use the tool 'Extract Study Info Tool' to extract:
        - subjects
        - number of days
        - weak subject

        Input:
        {user_input}

        Return ONLY JSON.
        """,
        agent=input_agent,
        expected_output="JSON with subjects, days, weak"
    )