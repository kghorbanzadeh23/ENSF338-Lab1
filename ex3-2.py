import json
import timeit
import numpy as np
import matplotlib.pyplot as plt

def read_write_json_files(input_file):
    # Load the input JSON file
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Change the size field in every record to the value 35
    for record in data:
        record['size'] = 35

if __name__ == "__main__":
    input_file = "large-file.json"
    
    # Lists to store data for linear regression
    list_lengths = []
    avg_times = []

    # Vary the number of records (1000, 2000, 5000, 10000)
    for num_records in [1000, 2000, 5000, 10000]:
        # Repeat each measure 100 times and compute the average time
        timed_function = lambda: read_write_json_files(input_file)
        time_taken = timeit.timeit(timed_function, number=100) / 100
        print(f'Average time taken for {num_records} records: {time_taken:.6f} seconds')

        # Append data for linear regression
        list_lengths.append(num_records)
        avg_times.append(time_taken)

    # Produce a linear regression plot
    slope, intercept = np.polyfit(list_lengths, avg_times, 1)
    plt.scatter(list_lengths, avg_times)
    line_values = [slope * x + intercept for x in list_lengths]
    plt.plot(list_lengths, line_values, 'r')

    # Save the plot to a file named output.3.2.png
    plt.xlabel('Number of Records')
    plt.ylabel('Average Processing Time (seconds)')
    plt.title('Linear Regression: Number of Records vs. Average Processing Time')
    plt.savefig('output.3.2.png')

    # Print the linear model
    print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))
