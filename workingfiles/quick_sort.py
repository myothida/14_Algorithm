def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:        
        while low <= high and array[high] >= pivot:
            high = high - 1        
        while low <= high and array[low] <= pivot:
            low = low + 1        
        if low <= high:
            array[low], array[high] = array[high], array[low]            
        else:            
            break
    
    array[start], array[high] = array[high], array[start]
    print(high, array)
    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
    
    return array

if __name__ == "__main__":
    # Example usage:
    unsorted_array = [1430, 3292, 7684, 1338, 193, 595, 4243, 9002, 4393, 130,1001] 
    sorted_array = quick_sort(unsorted_array, 0, len(unsorted_array) - 1)
    print("Sorted array:", sorted_array)