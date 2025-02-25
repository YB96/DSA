class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next
        print()  # This will print a new line after the linked list is printed

    def at_beginning(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head  # Set the next of new node to the current head
            self.head = new_node  # Update the head to the new node

    def at_end(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        c = self.head
        while c.next is not None:
            c = c.next
        c.next = new_node

    def insert(self,value,index):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

    def traversal(self):
        c = self.head
        while c is not None:
            print(c.value)
            c = c.next

    def search(self,target):  #for searching the target 
        c = self.head
        while c:
            if c.value == target:
                print(f"{target} is found,True")
                return
            c = c.next
        print(f"{target} is not found,False")    

    def get(self,index):    #passing an index and printing out the value
        if index < 0:
            raise IndexError("Index cannot be negative.")
        c = self.head
        if index == 0 and c is not None:
            print(f"At Index: 0 the value present is {c.value}.")
            return
        c = self.head
        i = 0
        while c:
            if i == index:
                print(f"At Index:{index} the value present is {c.value}.")
                return
            c = c.next
            i += 1
        return print(f"Index is out of range")
    
    def set_value(self,index,value):     #to update any value present in desired index
        c = self.head
        i = 0
        while c:
            if i == index:
                c.value = value
                return
            c = c.next
            i = i + 1
        return

    def pop_first(self):
        if self.head is None:
            print('Linked list is empty, so nothing to pop.')
            return
        first_node = self.head
        self.head = self.head.next #to point to second node
        first_node.next = None     #to break the relationship between nodes
        return first_node.value
    
    def pop(self):
        if self.head is None:
            raise IndexError("List is empty. Cannot pop.")
        if self.head.next is None:
            # If there is only one element in the list
            popped_value = self.head.value
            self.head = None
            return popped_value
        c = self.head
        while c.next.next is not None:
            c = c.next
        popped_value = c.next.value
        c.next = None
        return popped_value
    
    def remove(self, index):
        if index < 0:
            raise IndexError("Index cannot be negative.")
        if self.head is None:
            raise IndexError("List is empty. Cannot remove.")
        if index == 0:
            popped_value = self.head.value
            self.head = self.head.next
            return popped_value
        c = self.head
        for _ in range(index - 1):
            if c.next is None:
                raise IndexError("Index out of range.")
            c = c.next
        popped_value = c.next.value
        c.next = c.next.next
        return popped_value

    def delete_all_nodes(self):
        pass
        
    def reverse(self):
        current_node = self.head
        prev_node = None #prev_node is initially None, as the first node's next should be None after reversing.
        while current_node is not None:
            next_node = current_node.next #next_node is used to keep track of the next node before changing current_node.next.
            current_node.next = prev_node #current_node.next is set to prev_node, effectively reversing the pointer.
            prev_node = current_node
            current_node = next_node #Then, prev_node and current_node are updated to move to the next nodes in the list.
        self.head = prev_node #Finally, self.head is updated to the last node, which becomes the new head after reversal.




# Middle of a Singly Linked List
# Write a function to find and return the middle node of a singly linked list. 
# If the list has an even number of nodes, return the second of the two middle nodes.
    def middle(self):
        current_node = self.head
        i = 0
        while current_node:
            current_node = current_node.next
            i += 1
        #print(i)
        if i%2 == 0:
            for _ in range(0,(i//2)+1):
                current_node = self.head
                current_node = current_node.next
                v = current_node.next.next.value
            return v
        else:
            for _ in range(0,(i//2)+1):
                current_node = self.head
                current_node = current_node.next
                v = current_node.next.value
            return v
        
    def middle_1(self):  #efficient way to find the middle of a linked list
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def remove_duplicates(self):
        current = self.head
        while current is not None:
            # Compare current node with its next node
            runner = current
            while runner.next is not None:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
        return prev
    
    
    def remove_val(self, val):
        # Remove nodes from the beginning with the value
        while self.head is not None and self.head.value == val:
            self.head = self.head.next

        # Handle the rest of the list
        c = self.head
        while c is not None and c.next is not None:
            if c.next.value == val:
                c.next = c.next.next
            else:
                c = c.next
    
    def is_equal(self, list1, list2): #for palindrome
            while list1 and list2:
                if list1.value != list2.value:
                    return False
                list1 = list1.next
                list2 = list2.next
            return True
    
    def palindrome(self):
        # Save the original linked list
        original_head = self.head
        # Create a copy of the linked list
        copy_head = None
        curr = self.head
        while curr:
            node = Node(curr.value)
            node.next = copy_head
            copy_head = node
            curr = curr.next
        # Reverse one of the linked lists
        self.reverse()
        # Compare both linked lists
        is_palindrome = self.is_equal(original_head, copy_head)
        # Restore the original linked list
        #self.reverse()
        return is_palindrome

# Usage
ll = LinkedList()
ll.append(20)
ll.append(50)
#ll.at_beginning(30)
ll.at_end(20)
ll.print_list()
# ll.insert(70,3)
# ll.at_end(70)
# ll.print_list()
# print(ll.middle_1())
# #ll.remove_duplicates()
# ll.print_list()
# ll.reverse()
#ll.remove_val(40)
print(f"is it? {ll.palindrome()}")
ll.print_list()

# ll.traversal()
# ll.search(0)
# ll.get(0)
# ll.set_value(2,200)
# ll.print_list()
# popped_value = ll.pop_first()
# print(f"Popped value: {popped_value}")
# print("After popping:")
# ll.print_list()
#popped_value = ll.pop()
#print(f"Popped value: {popped_value}")
# print("After popping:")
#ll.print_list()
# remove_value = ll.remove(1)
# print(f'removed value : {remove_value}')
# ll.print_list()
# ll.middle()

print('-----------------------------')
ll2 = LinkedList()
ll2.append(10)
ll2.at_beginning(5)
ll2.at_end(15)
ll2.print_list()


def merge(l1, l2):
    l = []
    l11 = l1.head
    l22 = l2.head

    while l11 is not None and l22 is not None:
        if l11.value < l22.value:
            l.append(l11.value)
            l11 = l11.next
        else:
            l.append(l22.value)
            l22 = l22.next

    # Add remaining elements from l1, if any
    while l11 is not None:
        l.append(l11.value)
        l11 = l11.next

    # Add remaining elements from l2, if any
    while l22 is not None:
        l.append(l22.value)
        l22 = l22.next

    return sorted(l)
print(merge(l1=ll,l2=ll2))
print('---------------------------')

