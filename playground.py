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


def findPaths(self, m, n, N, i, j):
    """
    There is an m by n grid with a ball. Given the start coordinate (i,j)
    of the ball, you can move the ball to adjacent cell or cross the grid
    boundary in four directions (up, down, left, right). However, you can
    at most move N times. Find out the number of paths to move the ball out
    of grid boundary. The answer may be very large, return it after mod 10^9 + 7.
    m: int -- num rows in board
    n: int -- num cols in board
    N: int -- num moves allowed
    i: int -- initial row position
    j: int -- initial col position
    Solution uses top-down DP approach.
    """
    # 3D array storing num exits for a given position for a given number of steps
    mem = [[[-1 for _ in range(N)] for _ in range(n)] for _ in range(m)]
    def exit_move(row, col):
        return row >= m or col >= n or row < 0 or col < 0
    def update_mem(row, col, step, val):
        if mem[row][col][step]  < 0:
            mem[row][col][step] = val
        else:
            mem[row][col][step] += val
    def _findPaths(m, n, N, i, j):
        # if can't move, no paths exist
        if N <= 0:
            return 0
        # if in memory, return val
        if mem[i][j][N - 1] >= 0:
            return mem[i][j][N - 1]
        # move left
        left_paths = 0
        if exit_move(i, j - 1):
            left_paths = 1
        else:
            left_paths = _findPaths(m, n, N - 1, i, j - 1)
        # move right
        right_paths = 0
        if exit_move(i, j + 1):
            right_paths = 1
        else:
            right_paths = _findPaths(m, n, N - 1, i, j + 1)
        # move up
        up_paths = 0
        if exit_move(i + 1, j):
            up_paths = 1
        else:
            up_paths = _findPaths(m, n, N - 1, i + 1, j)
        # move down
        down_paths = 0
        if exit_move(i - 1, j):
            down_paths = 1
        else:
            down_paths = _findPaths(m, n, N - 1, i - 1, j)

        paths = sum([left_paths, right_paths, up_paths, down_paths])
        update_mem(i, j, N - 1, paths)
        return paths

    return _findPaths(m, n, N, i, j) % ((10 ** 9) + 7)
