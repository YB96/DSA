class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedlist:
    def __init__(self,value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def __str__(self):
        c = self.head
        r =''
        while c is not None:
            r += str(c.value)
            c = c.next
            if c == self.head:
                break
            r += "-->--"
        return (r)

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node        
        self.length += 1
    
    def at_beginning(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node # to make it circle
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
        
    def insert(self,value,index):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        elif index == 1:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
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

    

ll = CSLinkedlist(5)
ll.append(10)
ll.append(20)
ll.at_beginning(50)
ll.insert(2,1)
ll.traversal()
print(ll)