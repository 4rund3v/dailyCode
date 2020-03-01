# Tree
Basic Structure of a tree :
'''
struct node {
    int data;
    struct node* left;
    struct node* right;
}
'''


Tree is a nonlinear hierarchial data structure that consists of nodes connected by edges
A Tree consists of a 
    > Node
    > Edge

## Node
Node : an entity that contains a key or value and pointers to its child nodes.
The last nodes of each path are called leaf nodes or external nodes that do not contain a link/pointer to child nodes.
The node having at least a child node is called an internal node.

## Edge 
It is the link between any two nodes.

## Root 
It is the topmost node of a tree

The height of a node is the number of edges from the node to the deepest leaf (i.e. the longest path from the node to a leaf node.)

The depth of a node is the number of edges from the root to the node.

Degree of a node is the total number of branches of that node.

A collection of disjoint trees is called a forest.

Types of tree:
    > Binary Tree
    > Binary Search Tree
    > AVL Tree
    > B-Tree

Tree Traversal:
    > InOrder - First vist all the nodes in the left subtree, then the root node, visit the nodes in the right subtree.
        inorder(root -> left)
        display(root -> data)
        inorder(root -> left)

    > PreOrder - Visit the root node, vist all the nodes in the left subtree, visit all the nodes in the right subtree.
        display(root -> data)
        preorder(root -> left)
        preorder(root -> right)


    > PostOrder - Visit all the nodes in the left subtree, visit the root node, visit all the nodes in the right subtree.
        postorder (root -> left)
        postorder (root -> right)
        display (root -> data)


Tree Applications :
* Heap is a kind of tree that is used for heap sort.
* BSTs are used to quickly check whether an element is present in a set or not.
* A modern version of a tree called Tries is used in modern routers to store routing information.
* Most popular databases use Btrees and Ttrees which are variants of the tree structure to store their data.
* Compilers use a syntax tree to validate the syntax. 


