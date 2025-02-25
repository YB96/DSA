# FIFO - First in First out

#QUEUE with not list limit.
class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    def eneque(self,value):
        self.items.append(value)
        return "The element or value is inserted at the end of Queue."
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items.pop(0)
    
    def peak(self):  #to return 1st element of the list.
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items[0]
    
    def delete(self):
        self.items = None
        
customQueue = Queue()
print('-------------Queue----------------------')
print("Is the queue empty? ",customQueue.isEmpty())
customQueue.eneque(1)
customQueue.eneque(2)
customQueue.eneque(3)
customQueue.eneque(4)
print("The Queue is :",customQueue)
customQueue.dequeue()
print("The Queue after dequeue: ",customQueue)
print("Peak function of queue returns: ",customQueue.peak())

#QUEUE with list limit which is basically a circular queue.
class Queue_with_limit:
    def __init__(self,max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def isFull(self):
        if self.start + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False


print('-------------Queue with Limit----------------------')        
custom_queue = Queue_with_limit(3)
print(custom_queue.isFull())
print(custom_queue.isEmpty())
