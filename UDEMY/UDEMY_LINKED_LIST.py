class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):  #append method to add new node at the last
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    def __str__(self):
        c = self.head
        r = ''
        while c is not None:
            r = r + str(c.value)
            if c.next is not None:
                r = r + "-->>--"
            c = c.next
        return r 
    
    def at_begin(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self,value,index):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
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
        self.length += 1
    
    def traversal(self):
        c = self.head
        while c:
            print(c.value)
            c = c.next
    
ll = LinkedList(10)
ll.append(20)
ll.append(50)
ll.at_begin(30)
ll.insert(70,1)
ll.traversal()
print(ll)

