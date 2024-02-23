
import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def measure_running_time(arr):
    start_time = time.time()
    merge_sort(arr)
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
    numbers = [12, 3, 7, 9, 14, 6, 11, 2]
    print("Original list:", numbers)
    
    start_time = time.time()
    merge_sort(numbers)
    end_time = time.time()
    
    print("Sorted list:", numbers)
    print("Time taken:", end_time - start_time, "seconds")

    # Test with varying number of elements
    num_elements_list = [100, 500, 1000, 2000, 3000]
    sorted_running_time = []
    reverse_running_time = []

    for num_elements in num_elements_list:
        sorted_arr = list(range(num_elements))
        reverse_arr = list(range(num_elements, 0, -1)) 
        
        sorted_time = measure_running_time(sorted_arr)
        sorted_running_time.append(sorted_time)
        
        reverse_time = measure_running_time(reverse_arr)
        reverse_running_time.append(reverse_time)

    plot_running_time(num_elements_list, sorted_running_time, 'Merge Sort: Sorted Array')
    plot_running_time(num_elements_list, reverse_running_time, 'Merge Sort: Reverse Sorted Array')
