
# A LIFO stack for storing data.
class Stack:

    def __init__(self):
        self.stack = []

    # Places an item on the end of top of the stack
    def push(self, item):
        self.stack.append(item)

    # Removes a items from the top of the stack
    def pop(self):
        item = self.stack.pop()
        return item

    # Returns what is on the top of the stack without removing it
    def peek(self):
        item = self.stack[len(self.stack) - 1]
        return item

    # Returns true if the stack is empty or false if contains entries
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    # provides the number of stack items, not the total storage size of the stack.
    def size(self):
        stack_size = len(self.stack)
        return stack_size

