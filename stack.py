class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,data):
        return self.items.append(data)

    
    def pop(self):
        return self.items.pop()
    
s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)

print(s1.pop())



