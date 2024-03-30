class Queue: 
    def __init__(self) -> None:
        self.queue  = []
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    def enQueue(self, element):
        self.queue.append(element)
    
    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.queue.pop(0)
    def display(self):
        
        print(self.queue)
    def size(self):
        print(len(self.queue))
        
q = Queue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)

q.display()

q.deQueue()
print("After removing an element")
q.enQueue(10)
q.enQueue(20)
q.display()
q.deQueue()
print("After removing an element")
q.display()