import time
import random
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def measure_running_time(arr):
    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()
    return end_time - start_time

def plot_running_time(num_elements_list, running_time_list, title):
    plt.plot(num_elements_list, running_time_list, marker='o')
    plt.title(title)
    plt.xlabel('Number of Elements')
    plt.ylabel('Running Time (seconds)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    num_elements_list = [100, 500, 1000, 2000, 3000]
    sorted_running_time = []
    reverse_running_time = []

    for num_elements in num_elements_list:
        sorted_arr = list(range(num_elements))
        reverse_arr = list(range(num_elements, 0, -1))
        
        # Measure running time for sorted array
        sorted_time = measure_running_time(sorted_arr)
        sorted_running_time.append(sorted_time)
        
        # Measure running time for reverse sorted array
        reverse_time = measure_running_time(reverse_arr)
        reverse_running_time.append(reverse_time)

    plot_running_time(num_elements_list, sorted_running_time, 'Selection Sort: Sorted Array')
    plot_running_time(num_elements_list, reverse_running_time, 'Selection Sort: Reverse Sorted Array')
