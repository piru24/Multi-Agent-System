from tools.input_tool import extract_study_info
from agents.priority_agent import priority_agent
from agents.scheduler_agent import scheduler_agent

# take user input
user_input = input("Enter your study details: ")

# Step 1 – Input Agent
data = extract_study_info.run(user_input)

# Step 2 – Priority Agent
priority = priority_agent.run(data)

# Step 3 – Scheduler Agent (timetable)
state = scheduler_agent.run(data, priority)

print("\nExtracted Data:")
print(data)

print("\nPriority:")
print(priority)

print("\nFull state (subjects, priority, schedule):")
print(state)