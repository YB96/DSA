# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109


nums = [5, 7, 7, 8, 8, 10,13,73,8,89]
nums = sorted(nums)
target = 8
t1 = []

# nums = [1]
# target = 1

for i in range(len(nums)):
    if nums[i] == target:
        t1.append(i)

if not t1:
    t1 = [-1, -1]
t2 = [min(t1),max(t1)]
print(t1)
print(t2)

print("Second Solution")

nums = [5, 7, 7, 8, 8,8 ,8,8,8,10,13,73,8,89]
nums = sorted(nums)
target = 8

first_index = nums.index(target)

left = 0
right = len(nums) - 1
while left <= right:
    #print(nums[right])
    if nums[right] == target:
        last_index = right
        break
    right -= 1

print([first_index,last_index])

print("Solution 3")


mid = len(nums)//2
# print(len(nums))
# print(mid)
print(nums[:mid])
print(nums[mid:len(nums)])

print("-----------------------------------------")

print(nums[:mid])

indexes = []
left = 0
right = len(nums)
while left < mid:
    print(nums[left])
    if nums[left] == target:
        indexes.append(left)
        print("Index is ",left)
    left += 1



def findLeft(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def findRight(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right

left = findLeft(nums, target)
right = findRight(nums, target)

if left <= right:
    print([left, right])
else:
    print([-1, -1])