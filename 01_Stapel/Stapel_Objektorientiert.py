# LIFO

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.items)  # Output: Stack: [1, 2, 3]
print("Top element:", stack.peek())  # Output: Top element: 3
print("Popped element:", stack.pop())  # Output: Popped element: 3
print("Stack after pop:", stack.items)  # Output: Stack after pop: [1, 2]