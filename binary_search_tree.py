# Import the BSTNode class, which represents each node in the tree
from bst_node import BSTNode


class BinarySearchTree:
    """Binary Search Tree for storing variables and their integer values."""

    def __init__(self):
        # The root node of the tree (starts as empty)
        self.root = None

    def insert(self, key, value):
        # Public method to insert a key-value pair into the BST
        # Calls the recursive helper starting from the root
        self.root = self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node, key, value):
        # If we've reached an empty spot in the tree
        if node is None:
            # Create and return a new node
            return BSTNode(key, value)

        # If the new key is less than the current node's key
        if key < node.key:
            # Insert into the left subtree
            node.left = self._insert_recursive(node.left, key, value)

        # If the new key is greater than the current node's key
        elif key > node.key:
            # Insert into the right subtree
            node.right = self._insert_recursive(node.right, key, value)

        else:
            # If the key already exists, update the value
            node.value = value

        # Return the current node (important for linking the tree)
        return node

    def search(self, key):
        # Start searching from the root node
        current = self.root

        # Traverse the tree until we find the key or reach None
        while current is not None:

            # If the key matches the current node
            if key == current.key:
                # Return the associated value
                return current.value

            # If the key is smaller, go left
            elif key < current.key:
                current = current.left

            # If the key is larger, go right
            else:
                current = current.right

        # If we exit the loop, the key was not found
        raise KeyError(f"Variable '{key}' not found in BST.")

    def delete(self, key):
        # Public method to delete a node with the given key
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        # If we reached an empty node, nothing to delete
        if node is None:
            return None

        # If the key is smaller, search in left subtree
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)

        # If the key is larger, search in right subtree
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)

        else:
            # Node found — now handle deletion cases

            # Case 1: Node has no children (leaf)
            if node.left is None and node.right is None:
                return None  # simply remove it

            # Case 2: Node has only a right child
            if node.left is None:
                return node.right

            # Case 2: Node has only a left child
            if node.right is None:
                return node.left

            # Case 3: Node has two children
            # Find the smallest node in the right subtree
            successor = self._find_min(node.right)

            # Replace current node's data with successor's data
            node.key = successor.key
            node.value = successor.value

            # Delete the successor node from the right subtree
            node.right = self._delete_recursive(node.right, successor.key)

        # Return updated node
        return node

    def _find_min(self, node):
        # Start at given node
        current = node

        # Keep going left until there is no more left child
        while current.left is not None:
            current = current.left

        # Return the smallest node
        return current

    def delete_all(self):
        # Clear the entire tree by removing the root reference
        self.root = None

    def is_empty(self):
        # Return True if root is None (tree is empty)
        return self.root is None

    def display_tree(self):
        # If tree is empty, print message
        if self.root is None:
            print("[Tree is empty]")
        else:
            # Otherwise call recursive display helper
            self._display_recursive(self.root, 0)

    def _display_recursive(self, node, level):
        # If node exists
        if node is not None:

            # First display the right subtree (so it appears on top)
            self._display_recursive(node.right, level + 1)

            # Print current node with indentation based on level
            print("    " * level + f"{node.key}:{node.value}")

            # Then display the left subtree
            self._display_recursive(node.left, level + 1)