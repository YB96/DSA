#941. Valid Mountain Array
# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:
#     arr.length >= 3
#     There exists some i with 0 < i < arr.length - 1 such that:
#     arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
#     arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Example 1:
# Input: arr = [2,1]
# Output: false

# Example 2:
# Input: arr = [3,5,5]
# Output: false

# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
arr = [5,4,3,2]
def validMountainArray(arr):
    n = len(arr)
    # Step 1: Check if the array has at least 3 elements
    if n < 3:
        return False
    i = 0
    # Step 2: Traverse the array while it is strictly increasing
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1
    # Step 3: Check if i is the peak (i cannot be at the start or end)
    if i == 0 or i == n - 1:
        return False
    # Step 4: Traverse the array while it is strictly decreasing
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1
    # Step 5: If we've reached the end, it's a valid mountain array
    return i == n - 1
arr = [0, 2, 3, 4, 5]
print(validMountainArray(arr))  # Output: True
