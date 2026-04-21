import logging
logging.basicConfig(level=logging.INFO)

from agents.input_agent import input_agent
from agents.priority_agent import priority_agent
from agents.scheduler_agent import scheduler_agent
from agents.optimization_agent import optimization_agent

def run_pipeline(user_input: str):
    print("\n🚀 Starting Multi-Agent System...\n")

    # 🔹 Step 1: Input Agent
    study_data = input_agent.run(user_input)
    print("\n✅ Input Agent Output:", study_data)

    # 🔹 Step 2: Priority Agent
    priority = priority_agent.run(study_data)
    print("\n✅ Priority Agent Output:", priority)

    # 🔹 Step 3: Scheduler Agent
    state = scheduler_agent.run(study_data, priority)
    print("\n✅ Scheduler Output:", state["schedule"])

    # 🔹 Step 4: Optimization Agent
    final_state = optimization_agent.run(state)
    print("\n🔥 FINAL OPTIMIZED SCHEDULE:\n")

    for day in final_state["optimized_schedule"]:
        print(f"Day {day['day']}:")
        for session in day["sessions"]:
            print(f"  - {session['subject']} ({session['minutes']} mins)")
        print()

    return final_state


if __name__ == "__main__":
    user_input = input("Enter your study plan: ")
    run_pipeline(user_input)