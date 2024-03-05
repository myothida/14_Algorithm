from memory_profiler import profile

@profile
def recursive_function(n):
    if n <= 0:
        print("Reached base case.")
        return
    print(f"Function called with n = {n}")
    recursive_function(n - 1)
    print(f"Returning from function with n = {n}")

# Call the recursive function
recursive_function(3)