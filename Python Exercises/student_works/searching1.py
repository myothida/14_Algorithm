import time

def smallest_non_negative(arr):
    seen = set()
    result = []
    for num in arr:
        seen.add(num)
        smallest = 0
        while smallest in seen:
            smallest += 1
        result.append(smallest)
    return result

# Test cases
test_cases = [
    [0, 8, 7, 1, 1, 4, 3, 7, 0, 2],
    [1, 0, 5, 5, 3],
    [63, 46, 2, 66, 94, 58, 88, 82]
]

for idx, test_case in enumerate(test_cases, 1):
    print(f"Test Case {idx}:")
    start_time = time.time()
    print(smallest_non_negative(test_case))
    end_time = time.time()
    print(f"Running Time: {end_time - start_time:.6f} seconds")
    print()
