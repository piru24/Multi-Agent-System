import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.input_tool import extract_study_info


def test_extract_study_info():
    input_text = "I have Math and IT exam in 5 days, weak in Math"
    result = extract_study_info.run(input_text)

    assert "Math" in result["subjects"]
    assert "IT" in result["subjects"]
    assert result["days"] == 5
    assert result["weak"] == "Math"


def test_default_days():
    input_text = "I have Math exam"
    result = extract_study_info.run(input_text)

    assert result["days"] == 5  # default


def test_no_weak_subject():
    input_text = "I have IT exam in 3 days"
    result = extract_study_info.run(input_text)

    assert result["weak"] is None


if __name__ == "__main__":
    test_extract_study_info()
    test_default_days()
    test_no_weak_subject()
    print("✅ All Tests Passed!")