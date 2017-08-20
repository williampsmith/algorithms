class Tree:
	def __init__(self, root = None):
		self.root = root
		self.length = 0

	def printTree(self):
		def _printTree(root):
			if root == None:
				return
			else:
				_printTree(root.left)
				print(root.value)
				_printTree(root.right)
		_printTree(self.root)


	def insert(self, val):
		if self.root == None:
			self.root = Node(val)
			return

		current = self.root
		prev = None

		direction = None
		while current != None:
			if val < current.value:
				prev = current
				current = current.left
				direction = 0

			else:
				prev = current
				current = current.right
				direction = 1

		if direction: #right
			prev.right = Node(val)
		else:
			prev.left = Node(val)


class Node:
	def __init__(self, data = 0):
		self.value = data
		self.left = None
		self.right = None

def buildTree(ls):
	def _buildTree(ls, tree):
		for val in ls:
			tree.insert(val)

	tree = Tree()
	_buildTree(ls, tree)
	return tree






def similar(a, b):
	if a == None and b == None:
		return True
	elif a == None or b == None:
		return False

	if a.value != b.value:
		return False

	return (similar(a.left, b.left) and similar(a.right, b.right)) or (similar(a.right, b.left) and similar(a.left, b.right))

# node1 = Node(4)
# node1.left = Node(1)
# node1.right = Node(3)
# node1.right.left = Node(1)
# node1.right.right = Node(2)
# node1.left.left = Node(5)
# node1.left.right = Node(6)

# node2 = Node(4)
# node2.left = Node(3)
# node2.right = Node(1)
# node2.left.left = Node(1)
# node2.left.right = Node(3)
# node2.right.left = Node(6)
# node2.right.right = Node(5)

# node1 = Node(4)
# node1.left = Node(1)
# node1.right = Node(3)
# node1.right.left = Node(1)
# node1.right.right = Node(2)
# node1.left.left = Node(5)
# node1.left.right = Node(6)

# node2 = Node(4)
# node2.left = Node(3)
# node2.right = Node(1)
# node1.left.left = Node(1)
# node1.left.right = Node(2)
# node2.right.left = Node(6)
# node2.right.right = Node(5)

node1 = Node(4)
node1.left = Node(2)
node1.right = Node(3)

node2 = Node(4)
node2.left = Node(1)
node2.right = Node(3)

print(similar(node1, node2))
