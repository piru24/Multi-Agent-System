from tools.input_tool import extract_study_info
from agents.priority_agent import priority_agent

# take user input
user_input = input("Enter your study details: ")

# Step 1 – Input Agent
data = extract_study_info.run(user_input)

# Step 2 – Priority Agent
priority = priority_agent.run(data)

print("\nExtracted Data:")
print(data)

print("\nPriority:")
print(priority)