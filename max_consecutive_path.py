import pdb

def max_consecutive_path(root):
	def _max_consecutive_path(root, prev_val, prev_len):
		if root == None:
			return prev_len
		if root.val == prev_val + 1: # consecutive
			left_len = _max_consecutive_path(root.left, root.val, prev_len + 1)
			right_len = _max_consecutive_path(root.right, root.val, prev_len + 1)
			return max(left_len, right_len)
		else: # non-consecutive
			left_len = _max_consecutive_path(root.left, root.val, 1)
			right_len = _max_consecutive_path(root.right, root.val, 1)
			return max(prev_len, left_len, right_len)
	return _max_consecutive_path(root, root.val, 1)

class Node():
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def test():
	root = Node(10)
	root.left = Node(11)
	root.right = Node(9)
	root.left.left = Node(13)
	root.left.right = Node(12)
	root.left.right.right = Node(13)
	root.right.left = Node(13)
	root.right.right = Node(8)

	print('Maximum Consecutive Increasing Path Length is', max_consecutive_path(root))