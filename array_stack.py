"""
array_stack.py

Implements a stack using a Python list as the underlying dynamic array.
"""

from stack_interface import StackInterface


class ArrayStack(StackInterface):
    """Array-based stack implementation."""

    def __init__(self):
        """Create an empty stack."""
        self.data = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.data.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.data.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.data[-1]

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self.data) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.data)

    def __str__(self):
        """Return a string representation of the stack."""
        return str(self.data)
