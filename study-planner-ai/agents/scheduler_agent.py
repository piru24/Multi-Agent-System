from __future__ import annotations

import logging
from typing import Any

from crewai import Agent

from config import llm
from tools.scheduler_tool import generate_study_plan

logger = logging.getLogger(__name__)


class SchedulerAgent(Agent):
    """
    Builds a concrete timetable from extracted study data and priority scores.
    Uses ``generate_study_plan`` so scheduling is deterministic and testable.
    """

    def run(self, study_data: dict[str, Any], priority: dict[str, int]) -> dict[str, Any]:
        subjects = study_data.get("subjects") or []
        days = study_data.get("days", 1)

        logger.info("Scheduler input subjects=%s days=%s priority=%s", subjects, days, priority)

        plan = generate_study_plan(subjects=subjects, days=int(days), priority=priority)

        state: dict[str, Any] = {
            **study_data,
            "priority": priority,
            "schedule": plan["schedule"],
        }
        if study_data.get("weak") is not None:
            state["weak_subject"] = study_data["weak"]

        logger.info("Scheduler produced %d day(s) in schedule", len(plan["schedule"]))
        print("DEBUG → Scheduler state keys:", list(state.keys()))
        print("DEBUG → Schedule days:", len(plan["schedule"]))

        return state


scheduler_agent = SchedulerAgent(
    role="Study Scheduler",
    goal="Allocate time slots per day from subjects and priorities",
    backstory="You turn priorities into a balanced daily timetable using scheduling tools.",
    llm=llm,
    verbose=True,
)
