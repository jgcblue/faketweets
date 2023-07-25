
import math

def meanfromListof(thelist):
    total_y = 0
    for _, y in thelist:  # Here, _ is used as a throwaway variable for the first element of each tuple
        total_y += y
    mean_y = total_y / len(thelist)
    return mean_y

def calculate_mean_and_std_deviation(tuple_list):
    """
    Calculate the mean and standard deviation of the second coordinates (y-values) from a list of tuples.

    Args:
        tuple_list (list): A list of tuples.

    Returns:
        tuple: A tuple containing the mean and standard deviation of the y-values.
    """
    y_values = [y for _, y in tuple_list]

    mean_y = sum(y_values) / len(y_values)

    # Calculate the standard deviation
    variance = sum((y - mean_y) ** 2 for y in y_values) / len(y_values)
    std_deviation = math.sqrt(variance)

    return mean_y, std_deviation


