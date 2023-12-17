def calculate_spacing(max_value):
    """Determine grid spacing based on the maximum value."""
    if max_value < 10:
        return 1
    elif max_value < 50:
        return 5
    else:
        return 10
