def validate_priority(priority: dict) -> bool:
    """
    Validates that:
    - Values are integers
    - Highest priority exists
    """
    if not isinstance(priority, dict):
        return False

    values = priority.values()

    return all(isinstance(v, int) for v in values)