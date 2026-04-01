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
        # TODO: Append the item to self.data
        pass

    def pop(self):
        """Remove and return the top item from the stack."""
        # TODO: Check if stack is empty, then remove and return top item
        pass

    def peek(self):
        """Return the top item without removing it."""
        # TODO: Check if stack is empty, then return top item
        pass

    def is_empty(self):
        """Return True if the stack is empty."""
        # TODO: Return True if self.data has no items
        pass

    def size(self):
        """Return the number of items in the stack."""
        # TODO: Return the length of self.data
        pass

    def __str__(self):
        """Return a string representation of the stack."""
        return str(self.data)