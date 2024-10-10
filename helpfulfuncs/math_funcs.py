def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer whose factorial is to be calculated

    Returns:
        int: The factorial of the input number

    Raises:
        ValueError: If the input is a negative integer or not an integer
    """

    # Check if the input is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Base case: factorial of 0 is 1
    if n == 0:
        return 1

    # Calculate factorial iteratively
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
