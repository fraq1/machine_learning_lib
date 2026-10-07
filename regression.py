def regress(data):
    """Simple regression function."""
    if not data:
        return 0
    return sum(data) / len(data)

if __name__ == "__main__":
    print(regress([1, 2, 3]))
