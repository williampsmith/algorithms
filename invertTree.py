def invertTree(tree):
	if tree == None:
		return
	tree.left, tree.right = tree.right, tree.left 
	invertTree(tree.left)
	invertTree(tree.right)

class Node():
	def __init__(self):
		self.data = 0
		self.left = None
		self.right = None

