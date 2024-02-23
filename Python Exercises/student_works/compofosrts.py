import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

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

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def generate_arrays(size):
    sorted_arr = list(range(1, size + 1))
    unsorted_arr = random.sample(range(1, size + 1), size)
    reverse_arr = sorted_arr[::-1]
    return sorted_arr, unsorted_arr, reverse_arr

def measure_running_time(algorithm, arr):
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    return end_time - start_time

def plot_running_time(bubble_time, insertion_time, merge_time, quick_time, selection_time, title):
    plt.plot(sizes, bubble_time, label='Bubble Sort')
    plt.plot(sizes, insertion_time, label='Insertion Sort')
    plt.plot(sizes, merge_time, label='Merge Sort')
    plt.plot(sizes, quick_time, label='Quick Sort')
    plt.plot(sizes, selection_time, label='Selection Sort')
    plt.title(title)
    plt.xlabel('Array Size')
    plt.ylabel('Running Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    sizes = [155, 575, 1300, 2222, 3555]

    bubble_sorted_time = []
    insertion_sorted_time = []
    merge_sorted_time = []
    quick_sorted_time = []
    selection_sorted_time = []

    bubble_unsorted_time = []
    insertion_unsorted_time = []
    merge_unsorted_time = []
    quick_unsorted_time = []
    selection_unsorted_time = []

    bubble_reverse_time = []
    insertion_reverse_time = []
    merge_reverse_time = []
    quick_reverse_time = []
    selection_reverse_time = []

    for size in sizes:
        sorted_arr, unsorted_arr, reverse_arr = generate_arrays(size)

        bubble_sorted_time.append(measure_running_time(bubble_sort, sorted_arr.copy()))
        insertion_sorted_time.append(measure_running_time(insertion_sort, sorted_arr.copy()))
        merge_sorted_time.append(measure_running_time(merge_sort, sorted_arr.copy()))
        quick_sorted_time.append(measure_running_time(quick_sort, sorted_arr.copy()))
        selection_sorted_time.append(measure_running_time(selection_sort, sorted_arr.copy()))

        bubble_unsorted_time.append(measure_running_time(bubble_sort, unsorted_arr.copy()))
        insertion_unsorted_time.append(measure_running_time(insertion_sort, unsorted_arr.copy()))
        merge_unsorted_time.append(measure_running_time(merge_sort, unsorted_arr.copy()))
        quick_unsorted_time.append(measure_running_time(quick_sort, unsorted_arr.copy()))
        selection_unsorted_time.append(measure_running_time(selection_sort, unsorted_arr.copy()))

        bubble_reverse_time.append(measure_running_time(bubble_sort, reverse_arr.copy()))
        insertion_reverse_time.append(measure_running_time(insertion_sort, reverse_arr.copy()))
        merge_reverse_time.append(measure_running_time(merge_sort, reverse_arr.copy()))
        quick_reverse_time.append(measure_running_time(quick_sort, reverse_arr.copy()))
        selection_reverse_time.append(measure_running_time(selection_sort, reverse_arr.copy()))

    # Plotting
    plot_running_time(bubble_sorted_time, insertion_sorted_time, merge_sorted_time, quick_sorted_time, selection_sorted_time, 'Sorted Array')
    plot_running_time(bubble_unsorted_time, insertion_unsorted_time, merge_unsorted_time, quick_unsorted_time, selection_unsorted_time, 'Unsorted Array')
    plot_running_time(bubble_reverse_time, insertion_reverse_time, merge_reverse_time, quick_reverse_time, selection_reverse_time, 'Reverse Array')
