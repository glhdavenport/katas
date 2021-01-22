class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def pop(self):
        return self.stack.pop()


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)
    
    def dequeue(self):
        if self.stack2.size() == 0:
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()