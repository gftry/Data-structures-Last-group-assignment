"""
stack_interface.py

Defines the basic operations that any stack class should support.
This is optional in Python, but it helps organize the program.
"""


class StackInterface:
    """A simple stack interface/base class."""

    def push(self, item):
        """Add an item to the top of the stack."""
        raise NotImplementedError("push() must be implemented.")

    def pop(self):
        """Remove and return the top item from the stack."""
        raise NotImplementedError("pop() must be implemented.")

    def peek(self):
        """Return the top item without removing it."""
        raise NotImplementedError("peek() must be implemented.")

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        raise NotImplementedError("is_empty() must be implemented.")

    def size(self):
        """Return the number of items in the stack."""
        raise NotImplementedError("size() must be implemented.")