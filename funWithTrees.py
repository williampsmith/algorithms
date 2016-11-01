# FUN WITH TREES!!!!

def isValidBST(A):
    def _isValidBST(A, minVal, maxVal):
        if A == None:
            return True
        return A.val > minVal and A.val < maxVal and _isValidBST(A.left, minVal, A.val) and _isValidBST(A.right, A.val,  maxVal)
    return _isValidBST(A, -float('inf'), float('inf'))

def invertTree(root):
    if root == None:
        return root
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root
