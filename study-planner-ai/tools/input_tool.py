from crewai.tools import tool

@tool("Extract Study Info Tool")
def extract_study_info(text: str) -> dict:
    """
    Extract subjects, number of days, and weak subject from input text.
    """

    text = text.lower()

    subjects = []
    if "math" in text:
        subjects.append("Math")
    if "it" in text:
        subjects.append("IT")

    days = 5
    for word in text.split():
        if word.isdigit():
            days = int(word)

    subjects_list = ["Math", "IT"]

    weak = None
    for subject in subjects_list:
        if f"weak in {subject.lower()}" in text:
            weak = subject

    return {
        "subjects": subjects,
        "days": days,
        "weak": weak
    }