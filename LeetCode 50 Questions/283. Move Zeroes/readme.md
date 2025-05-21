# [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.</br>

📝 **Note:** You must do this *in-place* without making a copy of the array.

<details>
<summary>Example 1:</summary>

* Input: `nums = [0,1,0,3,12]`</br>
* Output: `[1,3,12,0,0]`
</details>

<details>
<summary>Example 2:</summary>

* Input: `nums = [0]`</br>
* Output: `[0]`
</details>

## Constraints:
- `1 <= nums.length <= 10⁴`</br>
- `-2³¹ <= nums[i] <= 2³¹ - 1`</br>

---

## Goal:
1. Traverse the array and identify non-zero elements.</br>
2. Shift non-zero elements forward in-place to maintain order.</br>
3. Fill the remaining positions with zeroes.</br>

<details>
<summary><strong style="font-size: 16px">Explanation:</strong></summary>

* Step 1: We initialize a pointer `lastNonZero = 0`, which keeps track of the index where the next non-zero element should be placed.
* Step 2: Loop through the array:
  - If the current element is non-zero, we **swap it** with the element at `lastNonZero` and increment `lastNonZero`.
* Step 3: This ensures all non-zero values are moved to the front in order, and zeroes are automatically pushed to the back.
* Step 4: Since the operation is in-place, we do not use extra memory.

</details>

---

## The Solution:
```python
def moveZeroes(self, nums):
    lastNonZero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[lastNonZero] = nums[lastNonZero], nums[i]
            lastNonZero += 1
```

---

<center>
<span style="font-size: 40px;color: #57B4BA;"> Thankyou </span> 
</center>
