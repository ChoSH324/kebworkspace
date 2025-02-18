class Stack:
    def __init__(self):
        self.items=list()

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(11)
print(s1.peek())
print(s1.size())
s1.pop()
print(s1.peek())
print(s1.size())