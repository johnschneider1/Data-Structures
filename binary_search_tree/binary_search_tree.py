from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # each node is a tree
    def insert(self, value):
        # nothing in the tree must add something, start on insert
        # if inserting we must already have a tree/root
        # if value is less than self.value go left, make a new tree/node if empth,
        # otherwise keep going(recursion)
        # if greater than or equal to
        # if root is none set root to node
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                # recurse to the left
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
                # recurse to the right

            else:
                self.right.insert(value)

        # pre follow along
        # if self.value == None:
        #     self.value = value
        #     return self.value
        # if self.value < value:

        #     if self.right is None:
        #         self.right = BinarySearchTree(value)
        #     else:
        #         return self.right.insert(value)
        # else:
        #     if self.left is None:
        #         self.left = BinarySearchTree(value)
        #     else:
        #         return self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if target == self.value, return it
        # else go left or right if smaller or bigger
        # base case
        if target == self.value:
            return True
            # if target is less than self.value we go left
        if target < self.value:
            if self.left is None:
                return False
            else:
                # recurse
                self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
                # return the recursion or you will lose state

        # pre follow
        #         # if target == self.value:
        #     return True
        # elif target < self.value and self.left is None:
        #     return False
        # elif target >= self.value and self.right is None:
        #     return False
        # elif target < self.value and self.left is not None:
        #     return self.left.contains(target)
        # elif target >= self.value and self.right is not None:
        #     return self.right.contains(target)

    # Return the maximum value found in the tree
    # if right exists, go right, else return self.value

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
