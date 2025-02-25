class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def merge(self, l1, l2):
        dummy = Node(None)  # Initialize dummy node with None
        tail = dummy

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next

    def print_list(self):
        current_node = self.head
        linked_list = []
        while current_node:
            linked_list.append(current_node.data)
            current_node = current_node.next
        print("Linked List:", linked_list)
        
    def intersection(self, l1, l2, v):
        dummy = Node()
        

# Example usage:

# Create a linked list object
linked_list = LinkedList()

# Example for insertAtBegin method
linked_list.insertAtBegin(0)
linked_list.print_list()  # Output: Linked List: [0]

# Example for insertAtEnd method
linked_list.insertAtEnd(4)
linked_list.print_list()  # Output: Linked List: [0, 4]

# Create two linked lists
list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)
# Example for merge method
merged_list_head = linked_list.merge(list1, list2)

# Create a new linked list with the merged list's head node
merged_linked_list = LinkedList()
merged_linked_list.head = merged_list_head

# Print the merged linked list
merged_linked_list.print_list()  

print(4//2)