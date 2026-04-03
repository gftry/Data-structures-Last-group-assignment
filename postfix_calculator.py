"""
postfix_calculator.py

Combines the stack and binary search tree to evaluate postfix expressions.
"""

from array_stack import ArrayStack
from binary_search_tree import BinarySearchTree


class PostfixCalculator:
    """Postfix calculator using a stack and BST."""

    def __init__(self):
        """Initialize the calculator with an empty stack and empty BST."""
        self.variable_tree = BinarySearchTree()
        self.stack = ArrayStack()

    def set_variable(self, key, value):
        """
        Store a variable and its value in the BST.

        Parameters:
            key (str): Variable name
            value (int): Variable value
        """
        # TODO: Insert variable into BST
        self.variable_tree.insert(key, value)
        pass

    def delete_all_variables(self):
        """Delete all variables from the BST."""
        # TODO: Clear the BST
        self.variable_tree.clear()
        pass

    def evaluate_postfix_expression(self, expression):
        """
        Evaluate a postfix expression and return the result.

        Parameters:
            expression (str): Postfix expression with tokens separated by spaces

        Returns:
            int: Final evaluated result
        """
        # TODO:
        # 1. Split expression into tokens
        # 2. Process each token
        # 3. Push integers or variable values onto stack
        # 4. Apply operators
        # 5. Return final result
        pass

    def is_operator(self, token):
        """Return True if token is a valid operator."""
        # TODO: Check for +, -, *, /
        pass

    def is_integer(self, token):
        """Return True if token can be converted to an integer."""
        # TODO: Try converting token to int
        pass

    def apply_operator(self, operator, left, right):
        """
        Apply an arithmetic operator to two operands.

        Parameters:
            operator (str): One of +, -, *, /
            left (int): Left operand
            right (int): Right operand

        Returns:
            int: Result of operation
        """
        # TODO: Perform the correct arithmetic operation
        pass
