def cluster(data, clusters=2):
    """Return the first requested number of data items."""
    if clusters <= 0:
        raise ValueError("clusters must be positive")
    return data[:clusters]
