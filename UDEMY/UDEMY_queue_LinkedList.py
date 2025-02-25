#FIFO - First In First Out
#Queue using Linked List.

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = new_node
            self.linkedlist.head = new_node
        else:
            self.linkedlist.tail.next = new_node
            self.linkedlist.tail = new_node 

custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)   
        
    

