class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        left = self.left.__repr__() if self.left else 'None'
        right = self.right.__repr__() if self.right else 'None'
        return '{ root: Node(' + str(self.val) + '), left: ' + left + ', right: ' + right + '}'

class BST:
    def __init__(self):
        self.root = None
