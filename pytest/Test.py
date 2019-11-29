import HOGenLibrary
from HOGenLibrary import Stack

s = Stack()
print(f"Is stack Empty {s.isEmpty()}")
s.push('Dog')
print(f"What is on top of stack {s.peek()}")
s.push(True)
print(f"Stack is {s.size()}")
print(f"Is stack Empty {s.isEmpty()}")
s.push(8.4)
print(f"What is on stack {s.pop()}")
print(f"What is on stack {s.pop()}")
print(f"Stack is {s.size()}")
