# Dictionary Interview Questions

# Q-1. What will be the output of the following code snippet?

a = {(1,2):1,
     (2,3):2}
print(a[1,2])
# A. Key Error
# B.  1
# C. {(2,3):2}
# D. {(1,2):1}
 

# Q-2. What will be the output of the following code snippet?

a = {'a':1,'b':2,'c':3}
# print (a['a','b'])
# A. Key Error
# B. [1,2]
# C. {‘a’:1,’b’:2}
# D. (1,2)

 

# Q-3. What will be the output of the following code block?

fruit = {}

def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
        
addone('Apple')
addone('Banana')
addone('apple')
print (len(fruit))
# A. 1 
# B. 2
# C. 3 
# D. 4

 

# Q-4. What will be the output of the following code block?

arr = {}
arr[1] = 1
arr['1'] = 2
arr[1] += 1

sum = 0
for k in arr:
    sum += arr[k]

print(sum)
# A. 1 
# B. 2
# C. 3 
# D. 4

 

# Q-5. What will be the output of the following code snippet?

my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4

sum = 0
for k in my_dict:
    sum += my_dict[k]
    
print (sum)
# A. 7
# B. Syntax error
# C. 3
# D. 6

 

# Q-6. What will be the output of the following code snippet?

my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12

sum = 0
for k in my_dict:
    sum += my_dict[k]

print (sum)
print(my_dict)
# A. Syntax error
# B. 30   
#     {(1, 2): 12, (4, 2, 1): 10, (1, 2, 4): 8}
# C. 47
#     {(1, 2): 12, (4, 2, 1): 10, (1, 2, 4): 8}
# D. 30
#     {[1, 2]: 12, [4, 2, 1]: 10, [1, 2, 4]: 8}

 

# Q-7. What will be the output of the following code snippet?

box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
# print(len(crates[box]))
# A. 1
# B. 3
# C. 4
# D. Type Error

 

# Q-8. What will be the output of the following code block?

dict = {'c': 97, 'a': 96, 'b': 98}

for _ in sorted(dict):
    print (dict[_])
# A. 96 98 97
# B. 96 97 98
# C. 98 97 96
# D. NameError

 

# Q-9. What will be the output of the following code snippet?

rec = {"Name" : "Python", "Age":"20"}
r = rec.copy()
print(id(r) == id(rec))
# A. True
# B. False
# C. 0
# D. 1

 

# Q-10. What will be the output of the following code snippet?

rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id1 == id2)
# A. True
# B. False
# C. 1
# D. Exception

print('-------------Q-Count Word Frequency-----------------')
# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.

# Example:
# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
# count_word_frequency(words) 
# Output:
#  {'apple': 3, 'orange': 2, 'banana': 1}
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
all_freq = {}
for i in words:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print(all_freq)
print('-----------Q-Common Keys------------')
#Common Keys
# Define a function with takes two dictionaries as parameters and merge them and sum 
# the values of common keys.

# Example:
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# merge_dicts(dict1, dict2)
# Output:{'a': 1, 'b': 5, 'c': 7, 'd': 5}
def merge_dicts(dict1, dict2):
    merged_dict = {}

    # Merge dict1 into merged_dict
    for key, value in dict1.items():
        merged_dict[key] = value

    # Update values or add new keys from dict2
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value

    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merged = merge_dicts(dict1, dict2)
print("Merged Dictionary:", merged)
print('-----------Key with the Highest Value--------------')
# Key with the Highest Value
# Define a function which takes a dictionary as a parameter and returns the key 
# with the highest value in a dictionary.

# Example:
# my_dict = {'a': 5, 'b': 9, 'c': 2}
# max_value_key(my_dict))
# Output: b
my_dict = {'a': 5, 'b': 9, 'c': 2}
m = max(my_dict.values())
for i in my_dict:
    if my_dict[i] == m:
        print(i)

print('----------------Reverse Key-Value Pairs------------------')
# Reverse Key-Value Pairs
# Define a function which takes as a parameter dictionary 
# and returns a dictionary in which everse the key-value pairs are reversed.

# Example:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# reverse_dict(my_dict)
# Output:{1: 'a', 2: 'b', 3: 'c'}
my_dict = {'a': 1, 'b': 2, 'c': 3}
print({v: k for k, v in my_dict.items()})

print('--------------Conditional Filter---------------')
# Conditional Filter
# Define a function that takes a dictionary as a parameter and returns a dictionary 
# with elements based on a condition.

# Example:
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
# filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0) 
# Output:{'b': 2, 'd': 4}
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
for i in my_dict:
    if my_dict[i] % 2 == 0:
        x = (my_dict[i])
print(x)