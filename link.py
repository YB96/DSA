class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def print(self):
        current = self.head
        while current is not None:
            print(current.value, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next
        print() 
        
    def at_begin(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head  
            self.head = new_node  

    def at_end(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        c = self.head
        while c.next is not None:
            c = c.next
        c.next = new_node

    def pop(self):
        if self.head is None:
            return None
        if self.head.next is None:
            pop_val = self.head.value
            self.head = None
            return pop_val
        c = self.head
        while c.next.next is not None:
            c= c.next
        pop_val = c.next.value
        c.next = None
        return pop_val
    
    def remove_duplicates(self):
        c = self.head
        while c is not None:
            r = c
            while r.next is not None:
                if r.next.value == c.value:
                    r.next = r.next.next
                else:
                    r = r.next
            c = c.next

    def reverse(self):
        c = self.head
        prev = None
        while c is not None:
            next_ = c.next
            c.next = prev
            prev = c
            c = next_
        self.head = prev


ll = LinkedList()
ll.at_begin(1)
ll.at_begin(2)
ll.at_end(3)
ll.at_end(4)
ll.at_end(4)
ll.print()
ll.reverse()
ll.print()
