""" n = int(input("List length = "))
list1 = []

for i in range(n):
    x = int(input("Elements  (0 a 9) = "))
    if (i == 0) or (x > list1[- 1]):
        list1.append(x)
    else:
        pos = 0
        while pos < len(list1):
            if x <= list1[pos]:
                list1.insert(pos, x)
                break
            pos = pos + 1

print(list1) """

l1 = [3,2,4,1,9,0,6]


def sort(list):
    pos = 0
    for i in range(len(list)):
        #print('i',i)
        for j in range(len(list)):
            #print('j',j)
            if list[i] < list[j]:
                pos = list[i]
                print('pos',pos)
                list[i] = list[j]
                print('list[j]:',list[j])
                list[j] = pos
    return list
print(sort(l1))



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Input array
arr = [5, 2, 8, 12, 3]
print(f'unsorted array: {arr}')

# Sorting the array using bubble sort
bubble_sort(arr)

# Displaying the sorted array
print("Sorted array in ascending order:", arr)
