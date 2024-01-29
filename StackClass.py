# This code creates a stack class
class Stack:
    def __init__(self):
        self.stack = []

    def push_to_stack(self, stack_value):
# Use list append method to add element
        if stack_value not in self.stack:
            self.stack.append(stack_value)
            return True
        else:
            return False

    # Use list pop method to remove element
    def pop_from_stack(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")

        else:
            return self.stack.pop()

# Use peek to look at the top of the stack
    def peek_in_stack(self):
        return self.stack[-1]

# AStack = Stack()
# AStack.push_to_stack("Mon")
# AStack.push_to_stack("Tue")
# AStack.peek_in_stack()
# print(AStack.peek_in_stack())
# AStack.push_to_stack("Wed")
# AStack.push_to_stack("Thu")
# print(AStack.peek_in_stack())
#
# print(AStack.pop_from_stack())
# print(AStack.pop_from_stack())