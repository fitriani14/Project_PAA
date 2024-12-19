import random
import matplotlib.pyplot as plt
import time

# Function to generate an array with random integers
def generate_array(n, max_val, seed):
    random.seed(seed)
    return [random.randint(0, max_val) for _ in range(n)]

# Function to check if array elements are unique
def is_unique(arr):
    return len(arr) == len(set(arr))

# Function to measure execution time of the uniqueness check
def measure_execution_time(arr):
    start_time = time.perf_counter()
    unique_status = is_unique(arr)
    end_time = time.perf_counter()
    return (end_time - start_time) * 1e6, unique_status  # Convert to microseconds

# Constants
max_value = 250 - 17  # Example for stambuk's last 3 digits = 017
n_values = [100, 150, 200, 250, 300]  # Adjusted to 5 values as per requirements
seed_base = 42  # Base seed for generating random seeds

# Variables to store results
worst_case_times = []
average_case_times = []
unique_status_list = []  # Store unique or non-unique status

# Main processing
for n in n_values:
    times = []
    for i in range(100):  # Run 100 trials to compute average case
        seed = seed_base + i  # Increment seed for each iteration
        arr = generate_array(n, max_value, seed)
        execution_time, unique_status = measure_execution_time(arr)
        times.append(execution_time)
        if i == 0:  # Store unique status for the first iteration only
            unique_status_list.append("Unique" if unique_status else "Non-Unique")

    # Simulate worst case by creating a fully non-unique array
    worst_case_arr = [1] * n
    worst_case_time, _ = measure_execution_time(worst_case_arr)

    worst_case_times.append(worst_case_time)
    average_case_times.append(sum(times) / len(times))

    print(f"n = {n}: Worst Case = {worst_case_time:.2f} us, Average Case = {sum(times) / len(times):.2f} us, First Array Status = {unique_status_list[-1]}")

# Save results to a text file
with open("worst_avg.txt", "w") as f:
    f.write("n,Worst Case (us),Average Case (us),First Array Status\n")
    for n, worst, avg, status in zip(n_values, worst_case_times, average_case_times, unique_status_list):
        f.write(f"{n},{worst:.2f},{avg:.2f},{status}\n")

# Plot graph
plt.figure(figsize=(10, 6))
plt.plot(n_values, worst_case_times, label="Worst Case", marker="o", color="red")
plt.plot(n_values, average_case_times, label="Average Case", marker="x", color="blue")
plt.xlabel("n (Array Size)")
plt.ylabel("Execution Time (us)")
plt.title("Execution Time Analysis")
plt.legend()
plt.grid()
plt.savefig("execution_time_plot.jpg")
plt.show()
