from bst import Node

empty_bst = None
trivial_bst = Node(5)
good_bst = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(5), Node(8)))
simple_bad_bst = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(5), Node(6)))
complex_bad_bst = Node(8, Node(6, Node(1), Node(7)), Node(9, Node(2), Node(13)))

def is_bst(root):
    def in_bounds(node, min, max):
        return min <= node.val <= max
    def _is_bst(node, min, max):
        """helper function for range checking"""
        if not node:
            return True
        return (
            in_bounds(node, min, max) and
            _is_bst(node.left, min, node.val) and
            _is_bst(node.right, node.val, max)
        )
    if not root:
        return True
    return _is_bst(root, -float('Inf'), float('Inf'))

def test_is_bst():
    print('Testing empty_bst is True...')
    assert(is_bst(empty_bst))
    print('Testing trivial_bst is True...')
    assert(is_bst(trivial_bst))
    print('Testing good_bst is True...')
    assert(is_bst(good_bst))
    print('Testing simple_bad_bst is False...')
    assert(not is_bst(simple_bad_bst))
    print('Testing complex_bad_bst is False...')
    assert(not is_bst(complex_bad_bst))
    print('OK!')

def in_order_traverse(node):
    if not node:
        return
    if node.left:
        in_order_traverse(node.left)
    print(node.val)
    if node.right:
        in_order_traverse(node.right)

def invert_bst(node):
    """ Inorder traversal should yield reverse sorted order"""
    if node:
        node.left, node.right = node.right, node.left
        map(invert_bst, (node.left, node.right))
        return node


def gcd(x, y):
    print('checking gcd(', x, ',', y, ')')
    if x < y:
        return gcd(y, x)
    if x == 0 and y == 0:
        return 0
    if y == 0:
        return x
    return gcd(x % y, y)

def compute_permutations(l):
    # TODO understand this -- EPI in Python pg. 230
    perms = []
    len_l = len(l)
    def _compute_permutations(l, i):
        if i == len_l - 1:
            perms.append(l.copy())
        for j in range(i, len_l):
            l[i], l[j] = l[j], l[i]
            _compute_permutations(l, i + 1)
            l[j], l[i] = l[i], l[j]
    _compute_permutations(l, 0)
    return perms
