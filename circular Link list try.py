class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedlist:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        c = self.head
        result =''
        while c is not None:
            result += str(c.value)
            c = c.next
            if c == self.head:
                break
            result += "-->--"
        return (result)

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            c = self.head
            while c.next != self.head:
                c = c.next
            c.next = new_node
            new_node.next = self.head
    
    def at_beginning(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            c = self.head
            new_node.next = self.head
            while c.next != self.head:
                c = c.next
            c.next = new_node
            self.head = new_node

    def insert(self,value,index):
        new_node = Node(value)
        if index == 0:
            if self.head is None:  #when the list is empty
                self.head = new_node
                new_node.next = self.head 
            else:
                c = self.head
                while c.next != self.head:
                    c = c.next
                c.next = new_node
                new_node.next = self.head
                self.head = new_node
        else:
            c = self.head
            for _ in range(index-1):
                c = c.next
            new_node.next = c.next
            c.next = new_node

    def traversal(self):
        c = self.head
        while c is not None:
            print(c.value)
            c = c.next
            if c == self.head:
                break
    
    def search(self,target):
        c = self.head
        while c is not None:
            if c.value == target:
                print("found")
            c = c.next
            if c == self.head:
                break
        print("not found")

    def get(self,index):
        c = self.head
        for _ in range(index):
            c = c.next
        print(c.value)    

    def set(self,index,value):
        if index == 0:
            self.head.value = value
        else:
            c = self.head
            i  = 0
            for _ in range(index):
                c = c.next
            c.value = value

    def pop_first(self):
        if self.head is None:
            print("Empty list")
            return None
        removed_node = self.head
        if self.head.next == self.head:  # Only one node in the list
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

        removed_node.next = None
        return removed_node.value
         
    def pop_last(self):
        if self.head is None:
            print("Empty list")
            return None
        removed_node = self.head
        if self.head.next == self.head:  # Only one node in the list
            self.head = None
        else:
            current = self.head
            while current.next.next != self.head: #designed to traverse the circular linked list to find the second-to-last node.
                current = current.next
            removed_node = current.next
            current.next = self.head
        removed_node.next = None
        return removed_node.value
    
    def remove(self,value):
        if self.head is None:
            return None
        if self.head.next == self.head:
            self.head = None
            
        prev = None
        current = self.head
        while True:
            if current.data == value:
                if prev is None:  # Removing the head node
                    prev = current
                    while prev.next != self.head:
                        prev = prev.next
                    prev.next = current.next
                    self.head = current.next
                else:
                    prev.next = current.next
                break
            prev = current
            current = current.next
            if current == self.head:  # Reached the end of the circular list
                break
    

    def delete_all(self):
        if self.head is None:
            return 
        if self.head.next == self.head:  # Only one node in the list
            self.head = None
            return
        current = self.head
        prev = None
        while True:
            if current.next == self.head:  # Reached the last node
                prev.next = None
                self.head = None
                break
            prev = current    
            current = current.next    # both to move forward.
    
    def reverse(self):
        pass 

    


ll = CSLinkedlist()
ll.append(10)
ll.append(15)
ll.append(20)
ll.at_beginning(5)
ll.at_beginning(0)
#ll.insert(2,1)
ll.traversal()
ll.search(50)
ll.get(0)
ll.set(2,50)
print(ll)
ll.pop_first()
ll.pop_last()
ll.remove(15)
print(ll)
        
