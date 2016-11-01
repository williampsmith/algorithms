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

def kthsmallest(self, root, k):
    def _kthsmallest(root, k, counter):
        if root == None:
            return None
        left = _kthsmallest(root.left, k, counter)
        if left != None:
            return left
        counter[0] = counter[0] + 1
        if k == counter[0]:
            return root.val
        return _kthsmallest(root.right, k, counter)
    return _kthsmallest(root, k, [0])

    # ---------------------------------  IN C++  -----------------------------------
    # int find(TreeNode* root, int &k) {
    #         if (!root) return -1;
    #         // We do an inorder traversal here. 
    #         int k1 = find(root->left, k);
    #         if (k == 0) return k1; // left subtree has k or more elements.
    #         k--; 
    #         if (k == 0) return root->val; // root is the kth element.
    #         return find(root->right, k); // answer lies in the right node.
    #     }

    #     int kthsmallest(TreeNode* root, int k) {
    #        return find(root, k); // Call another function to pass k by reference.
    #     }




