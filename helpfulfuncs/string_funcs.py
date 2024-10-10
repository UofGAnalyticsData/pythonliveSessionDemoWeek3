

def add_ed(input_string):
    """
    Append "ed" to a string if it does not already end with "ed"

    Args:
        input_string (str): A string to which ed is to be added

    Returns:
        str: A new string with "ed" appended if appropriate
    """

    # If the string already ends with ed
    # just return the string
    if input_string.lower().endswith("ed"):
        return input_string

    # add "ed" to the string and return
    return input_string + "ed"



def add_s(input_string):
    """
    Append "s" to a string if it does not already end with "s"

    Args:
        input_string (str): A string to which s is to be added

    Returns:
        str: A new string with "s" appended if appropriate
    """

    # If the string already ends with s 
    # just return the string
    if input_string.lower().endswith("s"):
        return input_string

    # add "s" to the string and return
    return input_string + "s"
