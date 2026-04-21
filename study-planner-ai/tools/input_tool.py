from crewai.tools import tool

@tool("Extract Study Info Tool")
def extract_study_info(text: str) -> dict:
    """
    Extract subjects, number of days, and weak subject from input text.
    """

    text = text.lower()

    # 🔥 Add more subjects
    possible_subjects = ["math", "it", "science", "english", "history"]

    subjects = []
    for subj in possible_subjects:
        if subj in text:
            subjects.append(subj.capitalize())

    # extract days
    days = 5
    for word in text.split():
        if word.isdigit():
            days = int(word)

    # 🔥 Better weak detection
    weak = None
    for subj in possible_subjects:
        if f"weak in {subj}" in text:
            weak = subj.capitalize()

    return {
        "subjects": subjects,
        "days": days,
        "weak": weak
    }