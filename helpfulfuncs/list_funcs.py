def is_sorted(lst):
    """
    Check if a list of integers is sorted in non-decreasing order.

    Args:
        lst (list): A list of integers to check.

    Returns:
        bool: True if the list is sorted in non-decreasing order, False otherwise.
    """

    # Check if the list is sorted by comparing each element with the next one
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
