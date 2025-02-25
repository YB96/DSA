# Create Simple Singly Linked List DS
# Write a code in the language of your choice to implement a singly linked list. A singly linked list has the following properties:
# 1.Each node contains a piece of data. Node class constructor  takes a value as an argument 
# and initializes the value attribute of the node.

# 2.Each node also holds a reference (or link) to the next node in the list. 
# A next attribute, initialized to None, which will store a reference to the next node in the list.

# 3.LinkedList class constructor  takes a value as an argument and creates new node object 
# based on Node class with that value.

# 4.head and tail attributes of the linked list to point to the new node.

# 5.A length attribute,initialized to 1, which represents the current number of nodes in the list.

class Node1:
    def __init__(self,data):
        self.value = data
        self.next = None

class Linkedlist1:
    def __init__(self,value):
        new_node = Node1(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1


# Insertion at the Beginning of a Singly Linked List
# Write a function to insert a new element at the beginning of a singly linked list. 
# LinkedList and Node class are already provided.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def at_begining(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def append(self,value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

# Deletion from a Singly Linked List
# Write a function to delete a node from a singly linked list and return deleted_node. 
# The function should take the index(starting from 0) of the node to be deleted as a parameter.

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
    
        # if node to be removed is the head node
        elif index == 0:
            popped_node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node
    
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
    
            popped_node = temp.next
            
            # if node to be removed is the tail node
            if popped_node.next is None:
                self.tail = temp
    
            temp.next = temp.next.next
            popped_node.next = None
            self.length -= 1
            return popped_node
        
#reverse the linked list 
        
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

#middle of a linked list
        
    def middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    