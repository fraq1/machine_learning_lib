def estimate(data):
    """Calculate the arithmetic mean."""
    if not data:
        return 0
    return sum(data) / len(data)
