from crewai import Agent
from config import llm
from tools.optimization_tool import optimize_schedule


class OptimizationAgent(Agent):
    def run(self, state: dict):
        print("DEBUG → Optimization input received")

        result = optimize_schedule(state)

        print("DEBUG → Optimization completed")

        return result


optimization_agent = OptimizationAgent(
    role="Schedule Optimizer",
    goal="Improve study schedule by balancing workload and adding breaks",
    backstory="You enhance schedules to make them more effective and realistic.",
    llm=llm,
    verbose=True
)