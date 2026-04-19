def validate_priority(data: dict) -> bool:
    """
    Validate priority output structure and values.

    Rules:
    - Must be a dictionary
    - Keys must be strings (subjects)
    - Values must be integers (1, 2, or 3)
    - Must contain exactly ONE highest priority (3)
    """

    if not isinstance(data, dict):
        return False

    if len(data) == 0:
        return False

    count_highest = 0

    for subject, priority in data.items():

        if not isinstance(subject, str):
            return False

        if not isinstance(priority, int):
            return False

        if priority not in [1, 2, 3]:
            return False

        if priority == 3:
            count_highest += 1

    # exactly one subject must have priority 3
    if count_highest != 1:
        return False

    return True