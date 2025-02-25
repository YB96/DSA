#LIFO - Last In First Out
#Stack using list and also without any limit.    
class Stack: 
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(i) for i in self.list]
        r = '\n'.join(values)
        return r

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self,value):  #is basically an append.
        return self.list.append(value)

    def pop(self):  #to remove last element
        return self.list.pop()

    def peek(self):
        return self.list[len(self.list)-1]


class Stack_with_limit:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = [] 

    def __str__(self):
        values = self.list.reverse()
        values = [str(i) for i in self.list]
        r = '\n'.join(values)
        return r 
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    def push(self,value):
        if self.isFull() == False:
            self.list.append(value)



stack = Stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
print(stack)
print('--------------------')
stack.pop()
print(stack.peek())