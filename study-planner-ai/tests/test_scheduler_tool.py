import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.scheduler_tool import generate_study_plan, validate_schedule


def test_schedule_has_correct_day_count():
    subjects = ["Math", "IT"]
    days = 5
    priority = {"Math": 3, "IT": 1}
    plan = generate_study_plan(subjects, days, priority)

    assert "schedule" in plan
    assert len(plan["schedule"]) == days


def test_all_subjects_in_each_day():
    subjects = ["Math", "IT"]
    days = 3
    priority = {"Math": 3, "IT": 2}
    plan = generate_study_plan(subjects, days, priority)

    for entry in plan["schedule"]:
        got = {s["subject"] for s in entry["sessions"]}
        assert got == set(subjects)


def test_higher_priority_gets_more_minutes_per_day():
    subjects = ["Math", "IT"]
    days = 1
    priority = {"Math": 3, "IT": 1}
    plan = generate_study_plan(subjects, days, priority)

    day1 = plan["schedule"][0]["sessions"]
    by_subject = {s["subject"]: s["minutes"] for s in day1}
    assert by_subject["Math"] > by_subject["IT"]


def test_validate_schedule_accepts_good_plan():
    subjects = ["Math", "IT"]
    days = 4
    priority = {"Math": 3, "IT": 1}
    plan = generate_study_plan(subjects, days, priority)
    assert validate_schedule(plan, subjects, days) is True


def test_generate_rejects_empty_subjects():
    try:
        generate_study_plan([], 5, {})
    except ValueError:
        return
    raise AssertionError("expected ValueError")


if __name__ == "__main__":
    test_schedule_has_correct_day_count()
    test_all_subjects_in_each_day()
    test_higher_priority_gets_more_minutes_per_day()
    test_validate_schedule_accepts_good_plan()
    test_generate_rejects_empty_subjects()
    print("All scheduler tool tests passed!")
