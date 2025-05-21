# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it '
# 'while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]
nums = [0,1,0,3,12]
# Solution 1 using for loop
# ele = 0
# nums.remove(ele)
# nums.append(ele)
# print(nums)
# c  = 0
# for i in range(len(nums)):
#     if nums[i] == ele:
#         c = c + 1
# print(c)
# for i in range(c):
#     nums.remove(ele)
#     nums.append(ele)
# print(nums)

# solution 2 - Two Pointer
left = 0
for right in range(len(nums)):
    if nums[right] != 0:
        nums[right], nums[left] = nums[left], nums[right]
        left += 1
print(nums)