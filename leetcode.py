import numpy as np
import string
import heapq
import re

# l1 =  ['abc', 'bca', 'ac']
# temp = 0
# for i in range(len(l1)):
#     for j in range(i):
#         if l1[i][j] == l1[i+1][j]:
#             pass


print('--------------------')
#1582 - leetcode
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
st = []
for i in range(len(indices)):
    st.insert(indices[i], s[i])
    print(indices[i], s[i])
print("".join(st))


print('---------------------------------')
#1773. Count Items Matching a Rule

items = [["phone","blue","pixel"],
         ["computer","silver","phone"],
         ["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"


res=0
for i in items:
    if ruleKey=="type":
        if i[0]==ruleValue:
            res+=1
        elif ruleKey=="color":
            if i[1]==ruleValue:
                res+=1
        elif ruleKey=="name":
            if i[2]==ruleValue:
                res+=1
print(res)

print('----------------------------')
#28 leetcode
haystack = "sadbutsad" 
needle = "sad"
haystack = "leetcode" 
needle = "leeto"

x = haystack.split(needle)
#x = x[0] 
print(x[0])
print(type(x))
print(any(len(ele) == 0 for ele in x))
print(haystack.find(needle))
        

print('--------------------')
#66 leetcode
digits = [1,2,3]
digits = [9]
d = ''.join(str(v) for v in digits)
d = int(d)
d = d + 1
print(int(d))
d = str(d)
print(type(d))
d = [*d]
d = [eval(i) for i in d]
print(d)


print('---------------------')
nums = [2,2,1]
#Output = 1
x ="".join(str(v) for v in nums)
#x = Counter(x)
print(x)
#print(min(list(x.values())))

print('---------------------')
#2325.Leetcode -  Decode the Message
st = string.ascii_lowercase
st = list(st)
print(list(st))
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
m1 = list(message)
print(m1)
#Output: "this is a secret"
#print(len(key))
#print(list(key))
l1 = list(key)
l1 = ' '.join(l1).split()
#print(l1)
#print(len(l1))
l1 = [i for n, i in enumerate(l1) if i not in l1[:n]]
print(l1)
print(len(l1))
res = {st[i]: l1[i] for i in range(len(st))}
print(res)
final = []
for char in message:
    if char == ' ':
        final.append(' ')
    # Check if the character is a value in the dictionary
    for key, value in res.items():
        if value == char:
            #print(f"Character '{char}' corresponds to key '{key}'")
            final.append(key)

print("".join(final))

print('---------------------')
#1662. Check If Two String Arrays are Equivalent

word1 = ["ab", "c"]
word2 = ["a", "b1c"]
#Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.
w1 = "".join(word1)
w2 = "".join(word2)
# print(w1)
# print(w2)
if w1 == w2:
    print(True)
else:
    print(False)

print('-------------------------------')
#1816. Truncate Sentence
# Input: s = "Hello how are you Contestant", k = 4
# Output: "Hello how are you"
# Explanation:
# The words in s are ["Hello", "how" "are", "you", "Contestant"].
# The first 4 words are ["Hello", "how", "are", "you"].
# Hence, you should return "Hello how are you".
s = "Hello how are you Contestant"
k = 4
#Output: "Hello how are you"
s = list(s.split(" "))
print(s[:k])
f = " ".join(s[:k])
print(f)

print('------------------------------')
#1859. Sorting the Sentence.
# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions 
# "This1 is2 a3 sentence4", then remove the numbers.
s = "is2 sentence4 This1 a3"
res = s.split()
print(res)
def compare_strings(s):
    return s[-1]
sorted_list = sorted(res, key=compare_strings)
sorted_list = [sub[: -1] for sub in sorted_list]
print(sorted_list)


print('---------------------')
#2828. Check if a String Is an Acronym of Words
# Input: words = ["alice","bob","charlie"], s = "abc"
# Output: true
# Explanation: The first character in the words "alice", "bob", and "charlie" 
# are 'a', 'b', and 'c', respectively. 
# Hence, s = "abc" is the acronym.
words = ["alice","bob","charlie"] 
s = "abc"
res = [sub[0] for sub in words]
print(res)
s1 = "".join(res)
print(s1)
print(s1==s)

print('--------------------------')
#1832. Check if the Sentence Is Pangram

# Example 1:
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:
# Input: sentence = "leetcode"
# Output: false
sentence = "thequickbrownfoxjumpsoverthelazydog"
sentence = list(sentence)
print(sentence)
st = string.ascii_lowercase
st = list(st)
st1 = sorted(sentence)
st2 = sorted(st)
print(st1)
print(len(st1))

res = []
[res.append(x) for x in st1 if x not in res]
print(res)
print(len(res))
print(st2)
print(res == st2)

print('----------------------------')
#1684. Count the Number of Consistent Strings

# Example 1:
# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 
# 'a' and 'b'.

# Example 2:
# Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# Explanation: All strings are consistent.

# Example 3:
# Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

allowed = "cad" 
words = ["cc","acd","b","ba","bac","bad","ac","d"]
allowed = set(allowed)
print(allowed)
count = 0
for i in words:
    if set(i).issubset(allowed):
        count = count + 1

print(count)

print('---------------------------')
#2810. Faulty Keyboard
# Input: s = "string"
# Output: "rtsng"
# Explanation: 
# After typing first character, the text on the screen is "s".
# After the second character, the text is "st". 
# After the third character, the text is "str".
# Since the fourth character is an 'i', the text gets reversed and becomes "rts".
# After the fifth character, the text is "rtsn". 
# After the sixth character, the text is "rtsng". 
# Therefore, we return "rtsng".
s = "string"
#s = "poiinter"
# Output: "rtsng"
#s = [s[i] for i in range(len(s))]
print(s)
indices = [i for i, s1 in enumerate(s) if 'i' in s1]
print(indices)

str1=""
for i in s:
    if i=="i":
        str1=str1[::-1]
    else:
        str1+=i
print(str1)
  
print('------------------------')
#88. Merge Sorted Array

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6] 
n = 3
l1 = []
for i in range(len(nums2)):
    l1.append(nums1[i])
    l1.append(nums2[i])

print(sorted(l1))
print('----Also can be done----')
for i in range(m,m+n):
        nums1[i]=nums2[i-m]
nums1.sort()

print('--------------------')
#1920. Build Array from Permutation

#Example 1:
# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# Explanation: The array ans is built as follows: 
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], 
#       nums[nums[4]], nums[nums[5]]]
#     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
#     = [0,1,2,4,5,3]
nums = [0,2,1,5,3,4]
res = []
for i in range(len(nums)):
    res.append(nums[nums[i]])

print(res)

print('----------------')
#1512. Number of Good Pairs

#Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
nums = [1,2,3,1,1,3]

c = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if i < j and nums[i] == nums[j]:
            c = c +1 
print(c)

print('----------------')
#2798. Number of Employees Who Met the Target

# Example 1:
# Input: hours = [0,1,2,3,4], target = 2
# Output: 3
# Explanation: The company wants each employee to work for at least 2 hours.
# - Employee 0 worked for 0 hours and didn't meet the target.
# - Employee 1 worked for 1 hours and didn't meet the target.
# - Employee 2 worked for 2 hours and met the target.
# - Employee 3 worked for 3 hours and met the target.
# - Employee 4 worked for 4 hours and met the target.
# There are 3 employees who met the target.
hours = [5,1,4,2,2]
target = 6
out = 0
for i in range(len(hours)):
    if hours[i] >= target:
        out += 1

print(out)

print('----------------------')
#1431. Kids With the Greatest Number of Candies

# Example 1:
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
candies = [2,3,5,1,3] 
extraCandies = 3
maximum = (max(candies))
e_candies = [(candies[i]+extraCandies) for i in range(len(candies))]
print(e_candies)

o = [e_candies[i] >= maximum for i in range(len(candies))]
print(o)

print('---------------------------')
#1672. Richest Customer Wealth

# Example 2:
# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation: 
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.

accounts = [[1,5],[7,3],[3,5]]
#print(sum(accounts[1]))
s = []
for i in range(len(accounts)):
    s.append(sum(accounts[i]))
print(max(s))

max_sum = max([sum(sublist) for sublist in accounts])
print(max_sum)

print('---------------------------')
#2824. Count Pairs Whose Sum is Less than Target

# Example 1:
# Input: nums = [-1,1,2,3,1], target = 2
# Output: 3
# Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
# - (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
# - (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target 
# - (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
# Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.

nums = [-1,1,2,3,1]
target = 2
n = len(nums)
s = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if (nums[i] + nums[j] < target) and 0 <= i < j < n:
            s = s + 1
print(s)

print('---------------')
#1480. Running Sum of 1d Array

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

nums = [1,2,3,4]
s = []
for i in range(1,len(nums)+1):
    s.append(sum(nums[:i]))

print(s)
s1 = [sum(nums[:i]) for i in range(1, len(nums) + 1)]
print(s1)

print('------------------')
#1365. How Many Numbers Are Smaller Than the Current Number

# Example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

nums = [8,1,2,2,3]

s = []

for i in range(len(nums)):
    temp = 0
    for j in range(len(nums)):
        if nums[j] < nums[i] and j != i:
            #8<1
            temp += 1
    s.append(temp)

print(temp)
print(s)

x = [sum(1 for other_num in nums if other_num < num) for num in nums]
print(x)

print('--------------')
#2574. Left and Right Sum Differences

# Example 1:
# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

nums = [10,4,8,3]
left = []
right = []
d = []
for i in range(len(nums)):       
    left.append(sum(nums[:i]))
    right.append(sum(nums[i+1:]))
        
print(left)
print(right)
for i in range(len(left)):
    d.append(abs(left[i] - right[i]))
print(d)

d = [abs(sum(nums[:i + 1]) - sum(nums[i:])) for i in range(len(nums))]
print(d)

print('----------------------')
#1389. Create Target Array in the Given Order

# Example 1:
# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# Explanation:
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
# 4            1        [0,4,1,3,2]
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
rei = []
for i in range(len(nums)):
    rei.insert(index[i],nums[i])

print(rei)

print('-----------------------------------')
#1720. Decode XORed Array

# There is a hidden integer array arr that consists of n non-negative integers.
# It was encoded into another integer array encoded of length n - 1, such that 
# encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], 
# then encoded = [1,2,3].
# You are given the encoded array. 
# You are also given an integer first, that is the first element of arr, i.e. arr[0].
# Return the original array arr. It can be proved that the answer exists and is unique.

# Example 1:
# Input: encoded = [1,2,3], first = 1
# Output: [1,0,2,1]
# Explanation: If arr = [1,0,2,1], then first = 1 and 
# encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
encoded = [1,2,3]
first = 1
result = []
for i in range(0, len(encoded)+1):
    if(i == 0):
        result.append(0^first)
    else:
        result.append(encoded[i-1]^result[i-1])
print(result)

print('----------------------')
#1313. Decompress Run-Length Encoded List

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
# Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so 
# we generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
nums = [1,2,3,4]
nums = [1,1,2,3]
generated = []  # just a starter array
for i in range(0, len(nums), 2):  # skip by 2 because...
    freq = nums[i]
    val = nums[i+1]  # that's why
    generated += [val] * freq  # shortcut to get freq vals

print(generated)

print('---------------------------')
#2535. Difference Between Element Sum and Digit Sum of an Array

# Example 1:
# Input: nums = [1,15,6,3]
# Output: 9
# Explanation: 
# The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.
nums = [1,15,6,3]
s1 = (sum(nums))
result_list = [int(digit) for number in nums for digit in str(number)]
s2 = sum(result_list)
d = abs(s1-s2)
print(d)

print('-------------------------------')
#2367. Number of Arithmetic Triplets

# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet 
# if the following conditions are met:
# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

# Example 1:
# Input: nums = [0,1,4,6,7,10], diff = 3
# Output: 2
# Explanation:
# (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
# (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
nums = [0,1,4,6,7,10] 
diff = 3
c = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if i < j < k and nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                c = c + 1

print(c)

print('-------------------------------------')
#1588. Sum of All Odd Length Subarrays

#Given an array of positive integers arr, 
# return the sum of all possible odd-length subarrays of arr.
# A subarray is a contiguous subsequence of the array. 

# Example 1:
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

arr = [1,4,2,5,3]
result = []
n = len(arr)

for start in range(n):
    for end in range(start, n):
        subarray = arr[start:end + 1]
        if len(subarray) % 2 == 1:
            result.append(subarray)

print(result)
final_sum = []
for i in range(len(result)):
    final_sum.append(sum(result[i]))

print(sum(final_sum))

print('-------------------------------')
#2006. Count Number of Pairs With Absolute Difference K

# Given an integer array nums and an integer k, return the number of pairs (i, j) 
# where i < j such that |nums[i] - nums[j]| == k.
# The value of |x| is defined as:
# x if x >= 0.
# -x if x < 0.

# Example 1:
# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
nums = [1,2,2,1]
k = 1
c = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if i < j and abs(nums[i] - nums[j]) == k:
            c = c + 1

print(c)

print('-----------------------')
#2373. Largest Local Values in a Matrix

# You are given an n x n integer matrix grid.
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid 
# centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 
# 3 x 3 matrix in grid.
# Return the generated matrix.

#Example 1:
# Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
# Output: [[9,9],[8,6]]
# Explanation: The diagram above shows the original matrix and the generated matrix.
# Notice that each value in the generated matrix corresponds to the largest 
# value of a contiguous 3 x 3 matrix in grid.
grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
N = len(grid)-2
res = [[0] * N for i in range(N)]
print(res)
for i in range(N):
    for j in range(N):
        res[i][j] = max([grid[r][c] for r in range(i, i+3) for c in range(j, j+3)])
print(res)

print('--------------------------')
#1572. Matrix Diagonal Sum

# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and 
# all the elements on the secondary diagonal that are not part of the primary diagonal.

# Example 1:
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
mat =   [[1,2,3],
        [4,5,6],
        [7,0,9]]
d1 = []
d2 = []
k = 0
k1= len(mat)-1
print(len(mat))
for i in range(len(mat)):
    d1.append(mat[i][k])
    k = k + 1 
print(d1) 
for i in range(len(mat)):
    d2.append(mat[i][k1])
    k1 = k1 - 1    
print(d2)
diagonal_sum = d1 + d2
res = []
[res.append(x) for x in diagonal_sum if x not in res]
print(diagonal_sum)
print(sum(res))

print('-------------------------')
# There is a biker going on a road trip. The road trip consists of n + 1 
# points at different altitudes. The biker starts his trip on point 0 with 
# altitude equal 0. You are given an integer array gain of length n where gain[i] is 
# the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). 
# Return the highest altitude of a point.

# Example 1:
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
#gain[i]=altitude[i+1]-altitude[i]
gain = [-5,1,5,0,-7]
print(gain)
current=0
highest=0
for x in gain:
    current+=x
    #print(current,highest)
    highest=max(current,highest)
print(highest)

ls=[]
k=0
ls.append(k)
for x in range(len(gain)):
    k+=gain[x]
    ls.append(k)
print(ls)
print(max(ls))

print('-------------------------')
#58. Length of Last Word
# Given a string s consisting of words and spaces, return 
# the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
s = "Hello World"
s = s.split()
print(len(s[-1]))

print('-----------------')
#125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
s = "A man, a plan, a canal: Panama"
s = s.lower()
new_str = re.sub(r'[\W_]', '', s)
s1 = (new_str)
s2 = (new_str[::-1])

print(s1 == s2)

print('---------------------')
#2656. Maximum Sum With Exactly K Elements 

# You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following 
# operation exactly k times in order to maximize your score:
# Select an element m from nums.
# Remove the selected element m from the array.
# Add a new element with a value of m + 1 to the array.
# Increase your score by m.
# Return the maximum score you can achieve after performing the operation exactly k times.

 

# Example 1:
# Input: nums = [1,2,3,4,5], k = 3
# Output: 18
# Explanation: We need to choose exactly 3 elements from nums to maximize the sum.
# For the first iteration, we choose 5. Then sum is 5 and nums = [1,2,3,4,6]
# For the second iteration, we choose 6. Then sum is 5 + 6 and nums = [1,2,3,4,7]
# For the third iteration, we choose 7. Then sum is 5 + 6 + 7 = 18 and nums = [1,2,3,4,8]
# So, we will return 18.
# It can be proven, that 18 is the maximum answer that we can achieve.
nums = [1,2,3,4,5]
k = 3
nums = sorted(nums)
m = nums[-1]
n = []
for i in range(k):
    n.append(m + i)
print(n)

print('-------------------------------')
# 832. Flipping an Image

# Given an n x n binary matrix image, flip the image horizontally, 
# then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0,1,1] results in [1,0,0].
 
# Example 1:
# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

image = [[1,1,0],[1,0,1],[0,0,0]]
print(image[0][::-1])
im = []
for i in range(len(image)):
    im.append(image[i][::-1])

modified_list = []
for i in range(len(im)):
    modified_list.append([1 if element == 0 else 0 if element == 1 else element for element in im[i]])
    
print(modified_list)

print('-----------------------------------------')
#1534. Count Good Triplets

# Given an array of integers arr, and three integers a, b and c. 
# You need to find the number of good triplets.
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
# Return the number of good triplets.

# Example 1:
# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
arr = [3,0,1,1,9,7] 
a = 7 
b = 2 
c = 3
xx = []
for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c and 0 <= i < j < k < len(arr):
                xx.append((arr[i],arr[j],arr[k]))

print(xx)

print('---------------------------------')
# The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).
# For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
# Given an integer array nums, choose four distinct indices w, x, y, and z such that the 
# product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.
# Return the maximum such product difference.

# Example 1:
# Input: nums = [5,6,2,7,4]
# Output: 34
# Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 
# for the second pair (2, 4).
# The product difference is (6 * 7) - (2 * 4) = 34.

nums = [5,6,2,7,4]
nums = sorted(nums)

n1 = nums[0]*nums[1]
print(n1)
n2 = nums[-1]*nums[-2]
print(n2)
d = n2-n1
print(d)

print('-----------------------------------------')
#15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
nums = [-1,0,1,2,-1,-4]
n = []
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                n.append([nums[i],nums[j],nums[k]])
print(n)
res = np.unique(np.array([np.sort(sub) for sub in n]), axis=0)
print(res.tolist())

print('----------------------------------------')
#557. Reverse Words in a String III

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace 
# and initial word order.
# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
s = "Let's take LeetCode contest"
s = s.split()
print(s[0][::-1])
s_new = [s[i][::-1] for i in range(len(s))]
print(" ".join(s_new))

print('---------------------------')
#2315. Count Asterisks

# You are given a string s, where every two consecutive vertical bars '|' 
# are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 
# 3rd and 4th '|' make a pair, and so forth.
# Return the number of '*' in s, excluding the '*' between each pair of '|'.
# Note that each '|' will belong to exactly one pair.

# Example 1:
# Input: s = "l|*e*et|c**o|*de|"
# Output: 2
# Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
# The characters between the first and second '|' are excluded from the answer.
# Also, the characters between the third and fourth '|' are excluded from the answer.
# There are 2 asterisks considered. Therefore, we return 2.

s = "l|*e*et|c**o|*de|"
s = (s.split('|'))
print(s)
even_elements = s[::2] 
print(even_elements)
s_new = "".join(even_elements)
print(s_new)
print(s_new.count('*'))
print('----------------------------------------------')
#1021. Remove Outermost Parentheses

# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B 
# are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a 
# way to split it into s = A + B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string s, consider its primitive decomposition: 
# s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
# Return s after removing the outermost parentheses of every primitive string 
# in the primitive decomposition of s.

# Example 1:
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

S = "(()())(())"
res, opened = [], 0
for c in S:
    if c == '(' and opened > 0: res.append(c)
    if c == ')' and opened > 1: res.append(c)
    opened += 1 if c == '(' else -1

print(res)
print("".join(res))
print('-------------------------------------------')
#2103. Rings and Rods

# There are n rings and each ring is either red, green, or blue. The rings are distributed across 
# ten rods labeled from 0 to 9.
# You are given a string rings of length 2n that describes the n rings that are placed onto the rods. 
# Every two characters in rings forms a color-position pair that is used to describe each ring where:
# The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
# The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
# For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, 
# a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.
# Return the number of rods that have all three colors of rings on them.

# Example 1:
# Input: rings = "B0B6G0R6R0R6G9"
# Output: 1
# Explanation: 
# - The rod labeled 0 holds 3 rings with all colors: red, green, and blue.
# - The rod labeled 6 holds 3 rings, but it only has red and blue.
# - The rod labeled 9 holds only a green ring.
# Thus, the number of rods with all three colors is 1.

rings = "B0B6G0R6R0R6G9"
print(re.split(r'\d+', rings))


print('-------------------------------------------------')
#16. 3Sum Closest

# Given an integer array nums of length n and an integer target, find three integers 
# in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

nums = [-1,2,1,-4]
target = 1
#not solving this test case.
nums = [0,1,2]
target = 3
l1 = []
for i in range(len(nums)):
    for j in range(i,len(nums)):
        for k in range(j,len(nums)):
            if nums[i] + nums[j] + nums[k] > target:
                x = nums[i],nums[j],nums[k]
                l1.append(x)

if l1 == []:
    l1.append((0,0,0))
print(l1)
print(min(l1))
print(sum(min(l1)))

print('-----------------------------------')
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

board =     [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
def is_valid_sudoku(b):
    def is_valid(nums):
        seen = set()
        for num in nums:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True

    for i in range(9):
        # Check rows
        if not is_valid(board[i]):
            return False
        
        # Check columns
        column = [board[j][i] for j in range(9)]
        if not is_valid(column):
            return False
print(is_valid_sudoku(board))

print('---------------------------------------------------')
#2859. Sum of Values at Indices With K Set Bits

# You are given a 0-indexed integer array nums and an integer k.
# Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly 
# k set bits in their binary representation.
# The set bits in an integer are the 1's present when it is written in binary.
# For example, the binary representation of 21 is 10101, which has 3 set bits.

# Example 1:
# Input: nums = [5,10,1,5,2], k = 1
# Output: 13
# Explanation: The binary representation of the indices are: 
# 0 = 0002
# 1 = 0012
# 2 = 0102
# 3 = 0112
# 4 = 1002 
# Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
# Hence, the answer is nums[1] + nums[2] + nums[4] = 13.
nums = [5,10,1,5,2]
k = 1
c=0
for i in range(len(nums)):
    if bin(i)[2:].count('1')==k:
        c+=nums[i]
print(c)

print('---------------------------------------')
#1844. Replace All Digits with Characters

# You are given a 0-indexed string s that has lowercase English letters in its even indices 
# and digits in its odd indices. There is a function shift(c, x), where c is a character and x is a digit,
# that returns the xth character after c.

# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).
# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

# Example 1:
# Input: s = "a1c1e1"
# Output: "abcdef"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('c',1) = 'd'
# - s[5] -> shift('e',1) = 'f'
s = "a1c1e1"
s = "a1b2c3d4e"
s = "v0g6s4d"
ss = ''
c  = ord(s[2-1]) + int(s[1])

for i in range(len(s)):
    if i%2==0:
        ss+=s[i]
    else:
        ss+=chr(ord(s[i-1])+int(s[i]))


print(ss)
print(chr(c))

print('--------------------------------')
#1768. Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the additional letters onto the end 
# of the merged string.
# Return the merged string

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s

# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
word1 = "ab" 
word2 = "pqrs"
new = []
l1 = len(word1)
l2 = len(word2)
print(l1>l2)

if l1 == l2:
    for i in range(len(word1)):
        new.append(word1[i])
        new.append(word2[i])
elif l2 > l1:
    for i in range(len(word1)):
        new.append(word1[i])
        new.append(word2[i])
    new.append(word2[l1:])
else:
    for i in range(len(word2)):
        new.append(word1[i])
        new.append(word2[i])
    new.append(word1[l2:])
print("".join(new))

print('------------------------------------------')
# Given an array of strings words, return the first palindromic string in the array. 
# If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

# Example 1:
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
#words = ["abc","car","ada","racecar","cool"]
#words = ["notapalindrome","racecar"]
#words = ["def","ghi"]
words = ["vhvqaqvhv","xefzzfex"]
l1 = []
for i in range(len(words)):
    if words[i] == words[i][::-1]:
            l1.append(words[i])
        # else:
        #     l1.append('')
print(l1)

if len(l1) == 0:
    x = ''
else:
    x = l1[0]
print(x)

print('-------------------------------------------------------------------')
#2710. Remove Trailing Zeros From a String
# Given a positive integer num represented as a string, return the integer num without trailing zeros 
# as a string.

# Example 1:
# Input: num = "51230100"
# Output: "512301"
# Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

# Example 2:
# Input: num = "123"
# Output: "123"
# Explanation: Integer "123" has no trailing zeros, we return integer "123".

num = "51230100"
#num = '123'
#num = "31514216007864075756059111751787923413952537015859352242147727420"
print(num.rstrip('0'))

print('-----------------------------------------')
#1812. Determine Color of a Chessboard Square

#You are given coordinates, a string that represents the coordinates of a square of the chessboard.
# Return true if the square is white, and false if the square is black.
# The coordinate will always represent a valid chessboard square. 
# The coordinate will always have the letter first, and the number second.

# Example 1:
# Input: coordinates = "a1"
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

# Example 2:
# Input: coordinates = "h3"
# Output: true
# Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.

# Example 3:
# Input: coordinates = "c7"
# Output: false

x = np.ones((3,3))
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(type(x[0][j]))
print((x))

xx = [[True if val == 0 else False for val in inner_list] for inner_list in x]  
print(xx)

coordinates = "c7"
#coordinates = "h8"
c1 = [ord(char) - ord('a') for char in coordinates[0]]
print(c1)
c1 = str(c1[0]) + coordinates[1:]
print(c1)

for i in range(len(xx)):
    for j in range(i+1):
        xxx = (xx[int(c1[0])][int(c1[1])])
print(xxx)

print('-----------------------------------------------')
#942. DI String Match

# A permutation perm of n + 1 integers of all the integers in the range [0, n] 
# can be represented as a string s of length n where:
# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. 
# If there are multiple valid permutations perm, return any of them.

# Example 1:
# Input: s = "IDID"
# Output: [0,4,1,3,2]

# Example 2:
# Input: s = "III"
# Output: [0,1,2,3]

# Example 3:
# Input: s = "DDI"
# Output: [3,2,0,1]
s = "IDID"
per=[]
lower=0
upper=len(s)
for i in s:
    if i=='I':
        per.append(lower)
        lower+=1
    else:
        per.append(upper)
        upper-=1
if s[len(s)-1]=='I':
    per.append(upper)
else:
    per.append(lower)
print(per)
print('-------------------------------------------')
#1704. Determine if String Halves Are Alike

# You are given a string s of even length. Split this string into two halves of equal lengths, and 
# let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels 
# ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and 
# lowercase letters.
# Return true if a and b are alike. Otherwise, return false.

# Example 1:
# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

# Example 2:
# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.

vo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
s = "book"
#s = "textbook"
print(len(s)//2)
s1 = (s[:len(s)//2])
s2 = (s[len(s)//2:])
c1 = 0
c2 = 0
for i in range(len(s1)):
    if s1[i] in vo:
        c1 += 1
    if s2[i] in vo:
        c2 += 1
print(c1)
print(c2)
print(c1==c2)
print('-----------------------------------------------')
# #2185. Counting Words With a Given Prefix
# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.

# Example 1:
# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

# Example 2:
# Input: words = ["leetcode","win","loops","success"], pref = "code"
# Output: 0
# Explanation: There are no strings that contain "code" as a prefix.
words = ["pay","attention","practice","attend"]
pref = "at"
co = 0
for i in range(len(words)):
    if words[i][:len(pref)] == pref:
        co += 1
print(co)
print('----------------------------------')
#1436. Destination City

# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a 
# direct path going from cityAi to cityBi. Return the destination city, that is, the city without
# any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore, 
# there will be exactly one destination city.

# Example 1:
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city.
# Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

# Example 2:
# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are: 
# "D" -> "B" -> "C" -> "A". 
# "B" -> "C" -> "A". 
# "C" -> "A". 
# "A". 
# Clearly the destination city is "A".

# Example 3:
# Input: paths = [["A","Z"]]
# Output: "Z"
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]




print('-------------------------------------')
#2748. Number of Beautiful Pairs

# You are given a 0-indexed integer array nums. A pair of indices i, j where 0 <= i < j < nums.length 
# is called beautiful if the first digit of nums[i] and the last digit of nums[j] are coprime.
# Return the total number of beautiful pairs in nums.
# Two integers x and y are coprime if there is no integer greater than 1 that divides both of them. 
# In other words, x and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor of
# x and y.

# Example 1:
# Input: nums = [2,5,1,4]
# Output: 5
# Explanation: There are 5 beautiful pairs in nums:
# When i = 0 and j = 1: the first digit of nums[0] is 2, and the last digit of nums[1] is 5. 
# We can confirm that 2 and 5 are coprime, since gcd(2,5) == 1.
# When i = 0 and j = 2: the first digit of nums[0] is 2, and the last digit of nums[2] is 1. Indeed, gcd(2,1) == 1.
# When i = 1 and j = 2: the first digit of nums[1] is 5, and the last digit of nums[2] is 1. Indeed, gcd(5,1) == 1.
# When i = 1 and j = 3: the first digit of nums[1] is 5, and the last digit of nums[3] is 4. Indeed, gcd(5,4) == 1.
# When i = 2 and j = 3: the first digit of nums[2] is 1, and the last digit of nums[3] is 4. Indeed, gcd(1,4) == 1.
# Thus, we return 5.

# Example 2:
# Input: nums = [11,21,12]
# Output: 2
# Explanation: There are 2 beautiful pairs:
# When i = 0 and j = 1: the first digit of nums[0] is 1, and the last digit of nums[1] is 1. Indeed, gcd(1,1) == 1.
# When i = 0 and j = 2: the first digit of nums[0] is 1, and the last digit of nums[2] is 2. Indeed, gcd(1,2) == 1.
# Thus, we return 2.

nums = [2,5,1,4]
nums = [11,21,12]
def gcd(x, y):
    count=0
    for i in range(1,max(x,y)+1):
        if x%i==0 and y%i==0:
            count+=1
    return count
c=0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) == 1:
            c+=1
print(c)

print('----------------------------------------------')

# 27. Remove Element.
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not 
# equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, 
# you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:
# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums 
# containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

nums = [3,2,2,3]
val = 3
while val in nums:
    nums.remove(val)
print(nums)    
print(len(nums))
print('--------------------------------------')

#70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
n = 3
def fibonacci_sum(n):
    fib_sequence = [0, 1]
    if n == 1:
        # Generate Fibonacci sequence up to n numbers
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        # Calculate the sum of the Fibonacci sequence
        fib_sum = sum(fib_sequence)
    else:
        # Generate Fibonacci sequence up to n numbers
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        
        # Calculate the sum of the Fibonacci sequence
        fib_sum = sum(fib_sequence) + 1
    return fib_sum 
# Example: Calculate the sum of the first 5 Fibonacci numbers
n = 1
result = fibonacci_sum(n)
print(result)
print('-----------------------------------')
# #189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, 
# where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
array = [1,2,3,4,5,6,7]
for i in range(k):
    #array1 = []
    array.insert(0,array[-1])
    array.pop()
    print(array)
print('-------------1051. Height Checker---------------')
#1051. Height Checker
# A school is trying to take an annual photo of all the students. 
# The students are asked to stand in a single file line in non-decreasing order 
# by height. Let this ordering be represented by the integer array expected where 
# expected[i] is the expected height of the ith student in line.
# You are given an integer array heights representing the current order that 
# the students are standing in. Each heights[i] is the height of the ith student 
# in line (0-indexed).
# Return the number of indices where heights[i] != expected[i].

# Example 1:
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

# Example 2:
# Input: heights = [5,1,2,3,4]
# Output: 5
# Explanation:
# heights:  [5,1,2,3,4]
# expected: [1,2,3,4,5]
# All indices do not match.

# Example 3:
# Input: heights = [1,2,3,4,5]
# Output: 0
# Explanation:
# heights:  [1,2,3,4,5]
# expected: [1,2,3,4,5]
# All indices match.
heights = [5,1,2,3,4]
c = 0
sor = sorted(heights)
for i in range(len(heights)):
    if heights[i] != sor[i]:
        c = c + 1
print(c)
print('---------------561. Array Partition------------------')
#561. Array Partition
# Given an integer array nums of 2n integers, 
# group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) 
# such that the sum of min(ai, bi) for all i is maximized. 
# Return the maximized sum.

# Example 1:
# Input: nums = [1,4,3,2]
# Output: 4
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.

# Example 2:
# Input: nums = [6,2,6,5,1,2]
# Output: 9
# Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). 
# min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
nums = [1,4,3,2]
nums = sorted(nums)
s = 0
for i in range(0,len(nums),2):
    print(i)
    s = s + nums[i]
print(s)
print('--------------2974. Minimum Number Game--------------------')
#2974. Minimum Number Game
# You are given a 0-indexed integer array nums of even length and there is also an empty array arr. 
# Alice and Bob decided to play a game where in every round Alice and Bob will do one move. 
# The rules of the game are as follows:

# Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
# Now, first Bob will append the removed element in the array arr, and then Alice does the same.
# The game continues until nums becomes empty.
# Return the resulting array arr.

# Example 1:
# Input: nums = [5,4,2,3]
# Output: [3,2,5,4]
# Explanation: In round one, first Alice removes 2 and then Bob removes 3. Then in arr firstly Bob appends 3 
# and then Alice appends 2. So arr = [3,2].
# At the begining of round two, nums = [5,4]. Now, first Alice removes 4 and then Bob removes 5. 
# Then both append in arr which becomes [3,2,5,4].

# Example 2:
# Input: nums = [2,5]
# Output: [5,2]
# Explanation: In round one, first Alice removes 2 and then Bob removes 5. 
# Then in arr firstly Bob appends and then Alice appends. So arr = [5,2].
nums = [5,4,2,3]
nums = [2,5]
# print(min(nums))
# p = nums.remove(min(nums))
# print(nums)
new_l = []
while nums:
    m = min(nums)
    nums.remove(m)
    new_l.append(m)
l = []
for i in range(len(new_l)//2):
    print(i)
    l1 = new_l[i*2:(i+1)*2]
    print(l1)
    l.append(l1[::-1])

res = [ele for sub in l for ele in sub]

print(l)
print(nums)
print(new_l)
print(res)
#another way
res=[]
nums = [5,4,2,3]
nums=sorted(nums)
for i in range(0,len(nums),2):
    res.extend(nums[i:i+2][::-1])
print(res)

print('----------------------------')
nums = [1,1,2,4,9]
print(nums)
k = 1
c = 0
print(all(i >= k for i in nums))
while nums[0] < k:
    c = c + 1
    nums.remove(min(nums))

#  longer way
# if all(i >= k for i in nums) == False:
#     for i in range(len(nums)):
#         k1 = nums.remove(min(nums))
#         print(nums)
#         for _ in range(len(nums)):
#             if all(i >= k for i in nums) == True:
#                 c = c + 1
# else:
#     c
# print(all(i >= k for i in nums))
print(c)
print('---------------2942. Find Words Containing Character-----------------')
#2942. Find Words Containing Character
# You are given a 0-indexed array of strings words and a character x.
# Return an array of indices representing the words that contain the character x.
# Note that the returned array may be in any order.

# Example 1:
# Input: words = ["leet","code"], x = "e"
# Output: [0,1]
# Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

words = ["abc","bcd","aaaa","cbc"]
x = "z"
l1 = []
for i in range(len(words)):
    if x in words[i]:
        l1.append(i)
print(l1)
print('--------------------------------')
nums = [13,25,83,77]
nums_str_final = []
#Output: [1,3,2,5,8,3,7,7]
nums_str = [str(i) for i in nums]
print(type(nums_str[0]))
print(nums_str[0][0])
for i in range(len(nums_str)):
    for j in range(len(nums_str[i])):
        nums_str_final.append(nums_str[i][j])

nums_str_final = [int(i) for i in nums_str_final]
print(nums_str_final)

print('---------------------------')
# 7 - Leetcode
x = -123
print(str(x)[:0:-1])
l1 = []
x = str(x)
if x[0] == '-':
    l1.append(x[0])
    l1.append(x[:0:-1])
elif int(x) in range(-2147483648, 2147483648):
    l1.append(x[::-1])
else:
    l1.append(str(0))
new_x = "".join(l1)
print(new_x)
new_x = int(new_x)
print(new_x)
print(type(new_x))
if new_x in range(-2147483648, 2147483648):
    new_x = new_x
else:
    new_x = 0
print(new_x)
print("---------905.Sort Array By Parity-------------")
#905. Sort Array By Parity
nums = [3,1,2,4]
nums_new = []
nums_new1 = []
for i in nums:
    if i % 2 == 0:
        nums_new.append(i)
    else:
        nums_new1.append(i)
f_list = nums_new + nums_new1
print(nums_new)
print(nums_new1)
print(f_list)
print('-------------------------')
#202. Happy Number
n = 19
n = str(n)
print(len(n))
# while True:
#     l1=[]
#     for i in range(len(n)):
#         l1.append((int(n[i])**2))
#         print(l1)


print('---------268------------')
nums = [0,1]
print(sorted(nums))
c = 0
for i in nums:
    if i == c:
        c = c + 1
    else:
        c
# print(c)
# nums = [1,7,10,5,6,8]
# c = nums[0]
# c1 = -1
# for i in range(len(nums)+1):
#     if c > nums[i]:
#         c1 = c
#         c = nums[i]
#     elif 
print('-----------------------------')