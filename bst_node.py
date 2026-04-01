"""
bst_node.py

Defines a node for the binary search tree.
Each node stores a variable name (key) and its integer value.
"""


class BSTNode:
    """Represents one node in the binary search tree."""

    def __init__(self, key, value):
        """
        Create a new BST node.

        Parameters:
            key (str): The variable name
            value (int): The value associated with the variable
        """
        self.key = key
        self.value = value
        self.left = None
        self.right = None