# 941. Valid Mountain Array
Given an array of integers arr, return true if and only if it is a valid mountain array.</br>
Recall that arr is a mountain array if and only if:</br>
* arr.length >= 3</br>

There exists some i with 0 < i < arr.length - 1 such that:</br>
* arr[0] < arr[1] < ... < arr[i - 1] < arr[i] </br>
* arr[i] > arr[i + 1] > ... > arr[arr.length - 1]</br>

<details>
<summary>Example 1:</summary>

* Input: arr = [2,1]</br>
* Output: false
</details>
<details>
<summary>Example 2: </summary>

* Input: arr = [3,5,5]</br>
* Output: false
</details>

## Goal:
1. First, check if the length of the array is at least 3.</br>
2. Find the peak of the mountain (i.e., the index where the array first stops increasing and starts decreasing).</br>
3. Ensure that the array strictly increases up to that peak and then strictly decreases after that peak.</br>

<details>
<summary>Explanation:</summary>

* Step 1: We first check if the length of the array is less than 3. If so, we return False because a valid mountain array must have at least 3 elements.
* Step 2: We start at the beginning of the array and check if each element is strictly smaller than the next. We continue incrementing i until we can't move forward in this strictly increasing part.
* Step 3: Once the loop ends, i should be the peak index. The peak index should not be the first (i == 0) or the last (i == n - 1) element. If it is, it means the array doesn't form a valid mountain, so we return False.
* Step 4: After finding the peak, we start a second loop to check if the remaining part of the array is strictly decreasing. If it is, we continue moving i.
* Step 5: Finally, if i reaches the last index (i == n - 1), it means we've successfully traversed the entire array, confirming it's a valid mountain array.
</details>

## The Solution:
```
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
print(validMountainArray(arr))
```