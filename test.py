l1 = [2,4,6,7,9,0,1,30]

#selection sort
def selection_sort(num1):
    for i in range(len(num1)):
        min_elemnet = i
        for j in range(i+1,len(num1)):
            if num1[j] < num1[min_elemnet]:
                min_elemnet = j
            num1[i], num1[min_elemnet] = num1[min_elemnet], num1[i]
    return num1
    
#print(selection_sort(l1))

#bubble sort 
#compares two adjacent elements and swaps them until they are in the intended order.
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j + 1]:
                # swapping elements if elements are not in the intended order
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


print('--------------------------------')
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def __str__(self):
        r = ''
        c = self.head
        while c:
            r = r + str(c.value)
            if c.next is not None:
                r = r + "-->>--"
            c = c.next
        return r
    
    def at_begin(self,value):
        new_node = Node(value)
        c = self.head
        if c is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def at_end(self,value):
        c = self.head
        new_node = Node(value)
        while c.next is not None:
            c = c.next
        c.next = new_node

    def pop(self):
        c = self.head
        while c.next.next is not None:
            c = c.next
        pop_val = c.next.value
        c.next = None
        return pop_val
    
    def length(self):
        count = 0
        c = self.head
        while c is not None:
            c = c.next
            count += 1
        return count
    
    def reverse(self):
        c = self.head
        prev = None
        while c is None:
            next_node = c.next
            c.next = prev
            prev = c
            c = next_node
        self.head = prev
    
    def remove(self,n):
        pass

ll = Linkedlist()
ll.at_begin(1)
ll.at_begin(2)
ll.at_end(3)
ll.at_end(4)
ll.at_begin(5)
print(ll)
ll.pop()
print(ll)
print(ll.length())
print(ll.reverse())

print("---------------------------")

l1 = [1,3,5,0,23,11,4,5]
l11 = []
for i in range(len(l1)):
    #print(l1[i])
    print(min(l1))
    l11.append(max(l1))
    l1.remove(max(l1))

print('---')
print(l11)
print("---------------------------")
l1 = [1,3,5,0,23,0,17,8]
for i in range(0,len(l1)):
    for j in range(0,len(l1)-i-1):
        if l1[j] > l1[j+1]:
            l1[j] , l1[j+1] = l1[j+1], l1[j]
print("Swapped list: ",l1)
print('---------------------------')

# Input: arr[] = {0, -1, 2, -3, 1}, target = -2
# Output: True
arr = [0, -1, 2, -3, 1]
tar = -2
def summ(arr, tar):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            #print(arr[i],arr[j])
            if arr[i] + arr[j] == tar:
                return True
    return False
print(summ(arr,tar))
print('--------------------------------')

arr = [0, -1, 4, 3, 1]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] > 4:
            print('greater tha 4')
        elif arr[i] + arr[j] == 4:
            print('equals to 4')
        else:
            print('Less than 4')

