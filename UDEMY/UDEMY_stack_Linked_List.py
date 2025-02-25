class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.Linkedlist = LinkedList() 
    
    def __str__(self):  #to print values in string and in a new line
        values = [str(x.value) for x in self.Linkedlist]
        return '\n'.join(values)

    def isEmpty(self):  #to check if the stack is empty or not
        if self.Linkedlist.head == None:
            return True
        else:
            return False
        
    def push(self,value):  #to add values on top of the stack
        node = Node(value)
        node.next = self.Linkedlist.head
        self.Linkedlist.head = node

    def pop(self):   #to remove topmost value of a stack
        if self.isEmpty():
            return "There is no value or element in the stack"
        else:
            nodeValue = self.Linkedlist.head.value
            self.Linkedlist.head = self.Linkedlist.head.next
            return nodeValue

    def peak(self):    #to return value of topmost element
        if self.isEmpty():
            return "There is no value or element in the stack"
        else:
            nodeValue = self.Linkedlist.head.value
            return nodeValue

    def delete(self):   #to delete every element or value in stack
        self.Linkedlist.head = None

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
print('----------')
print(f'value of topmost element is :{customStack.peak()}')
print(customStack.isEmpty())
print('-----------')
customStack.pop()
print(customStack)
print('----------')
print(f'value of topmost element is :{customStack.peak()}')
print(customStack)
print(customStack.delete())
print(customStack)
