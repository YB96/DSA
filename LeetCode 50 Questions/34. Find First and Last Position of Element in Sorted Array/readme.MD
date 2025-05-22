# [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.</br>

📝 **Note:** If `target` is not found in the array, return `[-1, -1]`.</br>  
You must write an algorithm with **O(log n)** runtime complexity.

<details>
<summary>Example 1:</summary>

* Input: `nums = [5,7,7,8,8,10], target = 8`</br>
* Output: `[3,4]`
</details>

<details>
<summary>Example 2:</summary>

* Input: `nums = [5,7,7,8,8,10], target = 6`</br>
* Output: `[-1,-1]`
</details>

<details>
<summary>Example 3:</summary>

* Input: `nums = [], target = 0`</br>
* Output: `[-1,-1]`
</details>

## Constraints:
- `0 <= nums.length <= 10⁵`</br>
- `-10⁹ <= nums[i] <= 10⁹`</br>
- `nums` is a non-decreasing array.</br>
- `-10⁹ <= target <= 10⁹`</br>

---

## Goal:
1. Traverse through the array and record the indexes where the target appears.</br>
2. If the target does not exist, return `[-1, -1]`.</br>
3. Else, return `[first_index, last_index]` using the recorded indices.</br>

<details>
<summary><strong style="font-size: 16px">Explanation:</strong></summary>

* Step 1: Initialize an empty list `t1` to hold the indices of the target.
* Step 2: Iterate through the array and add the index `i` to `t1` whenever `nums[i] == target`.
* Step 3: If `t1` is empty, it means the target was not found, so return `[-1, -1]`.
* Step 4: Otherwise, the result is `[min(t1), max(t1)]` representing the first and last occurrence.

</details>

---

## The Solution:
```python
nums = [5, 7, 7, 8, 8, 10]
target = 8
t1 = []

for i in range(len(nums)):
    if nums[i] == target:
        t1.append(i)

if not t1:
    t1 = [-1, -1]

t2 = [min(t1), max(t1)]
print(t1)  # All indices where target is found
print(t2)  # First and last index of the target
```

---

<center>
<span style="font-size: 40px;color: #57B4BA;"> Thankyou </span> 
</center>
