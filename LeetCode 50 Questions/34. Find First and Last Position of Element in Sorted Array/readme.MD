
# [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

---

<details>
<summary>Example 1:</summary>

* Input: `nums = [5,7,7,8,8,10]`, `target = 8`</br>
* Output: `[3,4]`
</details>

<details>
<summary>Example 2:</summary>

* Input: `nums = [5,7,7,8,8,10]`, `target = 6`</br>
* Output: `[-1,-1]`
</details>

<details>
<summary>Example 3:</summary>

* Input: `nums = []`, `target = 0`</br>
* Output: `[-1,-1]`
</details>

---

## Constraints:
- `0 <= nums.length <= 10⁵`</br>
- `-10⁹ <= nums[i] <= 10⁹`</br>
- `nums` is a non-decreasing array.</br>
- `-10⁹ <= target <= 10⁹`</br>

---

## 🔹 Solution 1: Using `index()` and reverse loop (Not O(log n), but simple)
```python
first_index = nums.index(target)

left = 0
right = len(nums) - 1
while left <= right:
    if nums[right] == target:
        last_index = right
        break
    right -= 1

print([first_index,last_index])
```
<details>
<summary>Explanation</summary>


### 🔍 Explanation:
- We use `index()` to get the first occurrence of the target.
- Then, we start a reverse loop from the end of the list to find the last occurrence.
- This is **not** O(log n) and can be slow for large inputs, but it’s a clear and simple solution.
</details>


---

## 🔹 Solution 2: Binary Search (Optimal - O(log n))
```python
def searchRange(nums, target):
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
            if nums[mid] == target:
                index = mid
        return index

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            if nums[mid] == target:
                index = mid
        return index

    return [findFirst(nums, target), findLast(nums, target)]
```
<details>
<summary>Explanation</summary>


### 🔍 Explanation:
- This approach uses binary search to find the **first** and **last** occurrences of the target value.
- `findFirst()` focuses on the leftmost position.
- `findLast()` focuses on the rightmost position.
- It works efficiently in O(log n) time.
</details>


---

<center>
<span style="font-size: 40px;color: #57B4BA;"> Thankyou </span> 
</center>
