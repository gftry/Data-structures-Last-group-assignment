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
        #Insert variable and its value into BST
        self.variable_tree.insert(key, value)
        pass

    def delete_all_variables(self):
        """Delete all variables from the BST."""
        #Resets calculator's memory by clearing tree
        self.variable_tree.delete_all()
        pass

    def evaluate_postfix_expression(self, expression):
        """
        Evaluate a postfix expression and return the result.

        Parameters:
            expression (str): Postfix expression with tokens separated by spaces

        Returns:
            int: Final evaluated result
        """

        #Converts the string into a list of strings
        tokens = expression.split()
        #Iterate through each token in the list
        for token in tokens:
            #If the token is a direct number, convert string to int and push it onto the stack
            if self.is_integer(token):
                self.stack.push(int(token))
            #If the token is an operator, pop the two items; apply the operator and push the result onto the stack
            elif self.is_operator(token):
                # Pop operands in reverse order (right then left)
                right = self.stack.pop()
                left = self.stack.pop()
                #Perform calculation and push the result onto the stack
                result = self.apply_operator(token, left, right)
                self.stack.push(result)
            else:
                # Assume it's a variable; look it up in the BST
                value = self.variable_tree.search(token)
                #Push the found value onto the stack
                self.stack.push(value)

        # The final result should be the only thing left on the stack
        return self.stack.pop()
    
        pass

    def is_operator(self, token):
        """Return True if token is a valid operator."""
        #Checks if the string matches one of the four operators
        return token in ('+', '-', '*', '/')
        pass

    def is_integer(self, token):
        """Return True if token can be converted to an integer."""
        #Return true if the token can be converted to an int
        try:
            int(token)
            return True
        #Return false if it can't be converted to an int
        except ValueError:
            return False
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
        #Perform arithmetic operation based on operator
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left // right # Using integer division for consistency
        return 0
        pass
