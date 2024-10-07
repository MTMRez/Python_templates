class Stack:
    stack = []
    def toStack(self,entry):
        self.stack.append(entry)
    def toUnstack(self):
        return self.stack.pop()
    def __str__(self):
        return str(self.stack)

stack0 = Stack()
stack0.toStack('enter-KEY')
stack0.toStack(245)
print(stack0)
print(stack0.toUnstack())
print(stack0)