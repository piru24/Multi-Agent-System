import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import run_pipeline


def test_full_pipeline_basic():
    input_text = "I have Math and IT exam in 5 days, weak in Math"

    result = run_pipeline(input_text)

    assert "optimized_schedule" in result
    assert len(result["optimized_schedule"]) == 5

    print("✅ Full pipeline basic test passed")


def test_full_pipeline_multiple_subjects():
    input_text = "I have Math, IT, Science exams in 6 days, weak in Science"

    result = run_pipeline(input_text)

    subjects = result["subjects"]
    assert "Science" in subjects
    assert result["weak"] == "Science"

    print("✅ Multi-subject test passed")


def test_full_pipeline_edge_case():
    input_text = "I have Science exam in 1 day, weak in Science"

    result = run_pipeline(input_text)

    assert len(result["optimized_schedule"]) == 1

    print("✅ Edge case test passed")


if __name__ == "__main__":
    test_full_pipeline_basic()
    test_full_pipeline_multiple_subjects()
    test_full_pipeline_edge_case()