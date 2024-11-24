def validate_positive_number(value, name="value"):
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError(f"{name} must be a positive number.")
    return value


def validate_non_negative_number(value, name="value"):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError(f"{name} must be a non-negative number.")
    return value
