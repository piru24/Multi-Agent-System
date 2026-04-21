from typing import Any

def optimize_schedule(state: dict[str, Any]) -> dict[str, Any]:
    """
    Final optimized version:
    - Normalize subject names
    - Rotate subjects
    - Add dynamic breaks
    - Reinforce weak subject
    - Add final revision day
    """

    schedule = state.get("schedule", [])
    weak = state.get("weak")

    optimized = []

    for i, day_plan in enumerate(schedule):

        sessions = day_plan["sessions"]

        # 🔥 Normalize subject names
        for s in sessions:
            if s["subject"].lower() == "it":
                s["subject"] = "IT"

        # 🔥 Reverse every other day (rotation)
        if i % 2 == 1:
            sessions = list(reversed(sessions))

        new_sessions = []

        for session in sessions:
            subject = session["subject"]
            minutes = session["minutes"]

            # 🔥 Reinforce weak subject
            if weak and subject == weak:
                minutes += 20  # extra time

            # 🔥 Dynamic break logic
            if minutes >= 90:
                break_time = 15
            elif minutes >= 60:
                break_time = 10
            else:
                break_time = 5

            new_sessions.append({
                "subject": subject,
                "minutes": minutes
            })

            new_sessions.append({
                "subject": "Break",
                "minutes": break_time
            })

        # remove last break
        if new_sessions and new_sessions[-1]["subject"] == "Break":
            new_sessions.pop()

        optimized.append({
            "day": day_plan["day"],
            "sessions": new_sessions
        })

    # 🔥 FINAL DAY = REVISION DAY
    subjects = state.get("subjects", [])
    revision_sessions = []

    for subj in subjects:
        if subj.lower() == "it":
            subj = "IT"

        revision_sessions.append({
            "subject": f"{subj} Revision",
            "minutes": 45
        })

    if len(optimized) > 1:
     optimized[-1] = {
        "day": optimized[-1]["day"],
        "sessions": revision_sessions
    }

    state["optimized_schedule"] = optimized
    return state