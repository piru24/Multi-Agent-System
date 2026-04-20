from __future__ import annotations

import math
from typing import Any


def generate_study_plan(
    subjects: list[str],
    days: int,
    priority: dict[str, int],
    *,
    minutes_per_day: int = 180,
) -> dict[str, Any]:
    """
    Build a day-by-day study timetable from subjects and priority weights.

    Higher priority values (1–3) receive a larger share of each day's study
    minutes. Minutes are split using integer allocation so totals match
    ``minutes_per_day`` per day.

    Args:
        subjects: Subject names to schedule (non-empty).
        days: Number of planning days (>= 1).
        priority: Map subject -> priority level (1, 2, or 3). Missing subjects
            default to priority 2.
        minutes_per_day: Total focused study minutes allocated per day.

    Returns:
        ``{"schedule": [{"day": int, "sessions": [{"subject": str, "minutes": int}, ...]}, ...]}``

    Raises:
        ValueError: If inputs are inconsistent or out of range.
    """
    if not isinstance(subjects, list) or not all(isinstance(s, str) for s in subjects):
        raise ValueError("subjects must be a list of strings")
    if len(subjects) == 0:
        raise ValueError("subjects must not be empty")
    if not isinstance(days, int) or days < 1:
        raise ValueError("days must be a positive integer")
    if not isinstance(priority, dict):
        raise ValueError("priority must be a dict")
    if not isinstance(minutes_per_day, int) or minutes_per_day < 1:
        raise ValueError("minutes_per_day must be a positive integer")

    for subj in subjects:
        p = priority.get(subj, 2)
        if not isinstance(p, int) or p not in (1, 2, 3):
            raise ValueError(f"priority for {subj!r} must be 1, 2, or 3")

    weights = [max(1, int(priority.get(s, 2))) for s in subjects]
    total_w = sum(weights)
    raw = [minutes_per_day * w / total_w for w in weights]
    base = [int(math.floor(x)) for x in raw]
    remainder = minutes_per_day - sum(base)
    frac_order = sorted(
        range(len(subjects)),
        key=lambda i: (raw[i] - base[i]),
        reverse=True,
    )
    day_minutes = list(base)
    for k in range(remainder):
        day_minutes[frac_order[k % len(subjects)]] += 1

    schedule: list[dict[str, Any]] = []
    for d in range(1, days + 1):
        sessions = [
            {"subject": subjects[i], "minutes": day_minutes[i]}
            for i in range(len(subjects))
            if day_minutes[i] > 0
        ]
        schedule.append({"day": d, "sessions": sessions})

    return {"schedule": schedule}


def validate_schedule(
    plan: dict[str, Any],
    subjects: list[str],
    days: int,
    *,
    minutes_per_day: int = 180,
) -> bool:
    """
    Check that a generated plan covers all days, includes every subject daily,
    and respects per-day minute totals.
    """
    if not isinstance(plan, dict) or "schedule" not in plan:
        return False
    sched = plan["schedule"]
    if not isinstance(sched, list) or len(sched) != days:
        return False
    seen_days: set[int] = set()
    for entry in sched:
        if not isinstance(entry, dict):
            return False
        day = entry.get("day")
        sessions = entry.get("sessions")
        if not isinstance(day, int) or not isinstance(sessions, list):
            return False
        if day in seen_days or day < 1 or day > days:
            return False
        seen_days.add(day)
        total = 0
        day_subjects: set[str] = set()
        for block in sessions:
            if not isinstance(block, dict):
                return False
            subj = block.get("subject")
            mins = block.get("minutes")
            if not isinstance(subj, str) or not isinstance(mins, int) or mins < 1:
                return False
            total += mins
            day_subjects.add(subj)
        if total != minutes_per_day:
            return False
        if day_subjects != set(subjects):
            return False
    return len(seen_days) == days
