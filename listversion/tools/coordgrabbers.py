
def get_first_coordinates(tuple_list):
    """
    Extract the first coordinates (x-values) from a list of tuples.

    Args:
        tuple_list (list): A list of tuples.

    Returns:
        list: A list containing the first coordinates (x-values).
    """
    x_values = [x for x, _ in tuple_list]
    return x_values
