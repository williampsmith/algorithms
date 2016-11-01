// C++ program to find the largest subtree
// having identical left and right subtree
#include <bits/stdc++.h>
#include <string>

using namespace std;
 
/* A binary tree node has data, pointer to left
  child and a pointer to right child */
struct Node
{
    int data;
    Node* left, * right;
};
 
/* Helper function that allocates a new node with
  the given data and NULL left and right pointers. */
Node* newNode(int data)
{
    Node* node = new Node;
    node->data = data;
    node->left = node->right = NULL;
    return (node);
}
 
// Sets maxSize to size of largest subtree with
// identical left and right.  maxSize is set with
// size of the maximum sized subtree. It returns
// size of subtree rooted with current node. This
// size is used to keep track of maximum size.

bool compareTrees(Node* a, Node* b){
    if(!a && !b) return true;
    if(!a || !b) return false;
    return ( (a->data==b->data) && (compareTrees(a->left,b->left)) && (compareTrees(a->right,b->right)) );
}

int largestSubtreeUtil(Node* root, int hash,
                    int& maxSize, Node*& maxNode)
{
    if (root == NULL)
        return 0;

    // int to store hashes of left and
    // right subtrees
    int lh = 0, rh=0;
 
    // traverse left subtree and finds its size
    int ls = largestSubtreeUtil(root->left, lh,
                               maxSize, maxNode);
 
    // traverse right subtree and finds its size
    int rs = largestSubtreeUtil(root->right, rh,
                               maxSize, maxNode);
 
    // if left and right subtrees are similar
    // update maximum subtree if needed (Note that
    // left subtree may have a bigger value than
    // right and vice versa)
    int size = ls + rs + 1;

    if (lh==rh && compareTrees(root->left,root->right))
    {
       if (size > maxSize)
       {
            maxSize  = size;
            maxNode = root;
       }
    }
    
    hash = lh ^ rh ^ root->data;        //XOR used as the hashing algorighm

    return size;
}
 
// function to find the largest subtree
// having identical left and right subtree
int largestSubtree(Node* node, Node*& maxNode)
{
    int maxSize = 0;
    int hash=0;
    largestSubtreeUtil(node, hash, maxSize, maxNode);
 
    return maxSize;
}
 
/* Driver program to test above functions*/
int main()
{
    /* Let us construct the following Tree
                50
              /     \
             10      60
            / \     /  \
            5 20   70   70
                   / \  / \
                  65 80 65 80   */
    Node* root = newNode(50);
    root->left = newNode(10);
    root->right = newNode(60);
    root->left->left = newNode(5);
    root->left->right = newNode(20);
    root->right->left = newNode(70);
    root->right->left->left = newNode(65);
    root->right->left->right = newNode(80);
    root->right->right = newNode(70);
    root->right->right->left = newNode(65);
    root->right->right->right = newNode(80);
 
    Node *maxNode = NULL;
    int maxSize = largestSubtree(root, maxNode);
 
    cout << "Largest Subtree is rooted at node "
         << maxNode->data << "\nand its size is "
         << maxSize;
 
    return 0;
}