import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.optimization_tool import optimize_schedule


def test_optimization():
    dummy_state = {
        "schedule": [
            {
                "day": 1,
                "sessions": [
                    {"subject": "Math", "minutes": 120},
                    {"subject": "IT", "minutes": 60}
                ]
            }
        ]
    }

    result = optimize_schedule(dummy_state)

    assert "optimized_schedule" in result
    assert len(result["optimized_schedule"]) == 1

    print("✅ Optimization Test Passed!")


if __name__ == "__main__":
    test_optimization()