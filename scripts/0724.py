import random
import statistics

def generate_random_data(size):
    return [(random.randint(1, 10), random.randint(1, 10000)) for _ in range(size)]

def find_outliers_with_mean(grouped_data, threshold=1.8):
    outliers_with_mean = {}

    for key, data_list in grouped_data.items():
        # Extract the second coordinates from the data list
        second_coordinates = [tpl[1] for tpl in data_list]

        # Calculate the mean and standard deviation of the second coordinates
        mean = statistics.mean(second_coordinates)
        std_dev = statistics.stdev(second_coordinates)

        # Define the threshold for outliers
        outlier_threshold = threshold * std_dev

        # Find outliers in the data list
        outliers = [tpl for tpl in data_list if abs(tpl[1] - mean) > outlier_threshold]

        outliers_with_mean[key] = (mean, outliers)

    return outliers_with_mean

# Generate a bigger dataset with 100 tuples
big_list_of_tuples = generate_random_data(1000)

# Create an empty dictionary to group tuples by their first elements
grouped_tuples = {}

# Group the tuples based on their first elements
for tpl in big_list_of_tuples:
    first_element = tpl[0]
    if first_element in grouped_tuples:
        grouped_tuples[first_element].append(tpl)
    else:
        grouped_tuples[first_element] = [tpl]

# Find outliers and mean for each key
outliers_with_mean = find_outliers_with_mean(grouped_tuples)

# Print the result
for key, (mean, outliers) in outliers_with_mean.items():
    print(f"Key: {key}, Mean: {mean}, Outliers: {outliers}")


