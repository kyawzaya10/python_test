class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items [len(self.items)-1]

mv = Stack()

mv.push("Oppenheimer")
mv.push("Barbie")
mv.push("The Flash")
print(mv.pop())