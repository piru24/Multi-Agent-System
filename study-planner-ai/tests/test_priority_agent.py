from agents.priority_agent import priority_agent

def test_priority():
    data = {
        "subjects": ["Math", "IT"],
        "days": 5,
        "weak": "Math"
    }

    result = priority_agent.run(data)

    assert "Math" in result
    assert "IT" in result

    print("Test passed!")

test_priority()