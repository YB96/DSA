class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
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
    
    def append(self, value):
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
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node


