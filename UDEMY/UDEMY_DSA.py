# 1.Missing Number
# Write a function to find the missing number in a given integer array of 1 to 100.

# Example:
# missing_number([1, 2, 3, 4, 6], 6) # 5
arr = []
for i in range(0,100):
    arr.append(i)
print(arr)
arr.remove(5)
print(arr)
for i in (arr):
    total = i * (i+1)//2
print(total)
print(sum(arr))

missing_number = total - sum(arr)
print(f'Missing number is {missing_number}')
print('----------------------------------------')

# 2.Middle Function
# Write a function called middle that takes a list and returns a new list that contains 
# all but the first and last elements.

# myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]
myList = [1, 2, 3, 4]
mid = len(myList)//2
print([myList[mid-1],myList[mid]])

print('----------------------------')
# 2D Lists
# Given 2D list calculate the sum of diagonal elements.
# Example
# myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
# diagonal_sum(myList2D) # 15

myList2D= [[1,2,3],
           [4,5,6],
           [7,8,9]]
sum1 = []
total = 0
for i in range(len(myList2D)): #oneway
    sum1.append(myList2D[i][i])

for i in range(len(myList2D)):  #secondway
    total = total + myList2D[i][i]
print(sum(sum1))
print(total)
print('----------------------------')

# Best Score
# Given a list, write a function to get first, second best scores from the list.
# List may contain duplicates.

# Example
# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# first_second(myList) # 90 87
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

for i in range(len(myList)):  #bubble sort
    for j in range(len(myList)-i-1):
        if myList[j] > myList[j+1]:
            myList[j], myList[j+1] = myList[j + 1], myList[j]

print(myList[::-1][:2])

print('-----------------------')

def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')
 
    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
 
    return max1, max2
 
my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list)) 

print('---------------------------------------')
# Duplicate Number
# Write a function to remove the duplicate numbers on given integer array/list.

# Example
# remove_duplicates([1, 1, 2, 2, 3, 4, 5])
# Output : [1, 2, 3, 4, 5]
remove_duplicates = [1, 1, 2, 2, 3, 4, 5]
out = []
s = set()
print(remove_duplicates)
for i in remove_duplicates:
    if i not in s:
        out.append(i)
        s.add(i)
print(out)
print('----------------------------')
# Pairs
# Write a function to find all pairs of an integer array whose sum is 
# equal to a given number. Do not consider commutative pairs.

# Example
# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']
pair_sum = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
num = 7
pairs =[]
n = len(pair_sum)
for i in range(n):
    for j in range(i+1,n):
        pairs.append((pair_sum[i],pair_sum[j]))
#print(pairs)
final_list = []
for i in pairs:
    if sum(i) == num:
        final_list.append(i)
print(final_list)

#Another way
result = []
for i in range(n):
    for j in range(i+1,n):
        if pair_sum[i] + pair_sum[j] == num:
            result.append(f"{pair_sum[i]}+{pair_sum[j]}")
print(result)
print('------------------------')
# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice 
# in the array, and return false if every element is distinct.

# Example :
# Input: nums = [1,2,3,1]
# Output: true
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(contains_duplicate(nums)) 
print('---------------------------')

# Rotate Matrix/ Image - LeetCode 48
# You are given an n x n 2D matrix representing an image, 
# rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the 
# input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

# Example:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
matrix1 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
def rotate_90(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):  # Iterate over the rows
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
            # Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row
print(rotate_90(matrix1))
print('-----------------------------------')
# Sum and Product
# Write a function that calculates the sum and product of all elements in 
# a tuple of numbers.

# Example
# input_tuple = (1, 2, 3, 4)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, product_result)  # Expected output: 10, 24
t = (1, 2, 3, 4)
sum_result = 0
product_result = 1
for num in t:
    sum_result += num
    product_result *= num
print(sum_result,product_result)
print('---------------------------------------')
# Elementwise Sum
# Create a function that takes two tuples and returns a tuple containing 
# the element-wise sum of the input tuples.

# Example
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)  # Expected output: (5, 7, 9)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
for i in range(len(tuple1)):
    t = (tuple1[i]+tuple2[i])
print(t)
print(tuple(map(sum, zip(tuple1, tuple2))))