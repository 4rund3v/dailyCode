#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g   
"""


class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None


def print_preorder(root_node):
    """
      Given a root node, prints the preorder traversal of that node
      Pre order traversal:
          Root --> Left --> Right
      Use cases :
          Prefix mathematical expressions
                       + 2 3
          Copying a tree
    """
    if root_node:
        print('  {}  '.format(root_node.value))
        print_preorder(root_node.left)
        print_preorder(root_node.right)
    return


def print_inorder(root_node):
    '''
     Given a root node, prints the inorder traversal of the node
     Inorder traversal :
          Left -> Root -> Right
     Usecases :
        Binary search trees
    '''
    if root_node:
        print_inorder(root_node.left)
        print('  {}  '.format(root_node.value))
        print_inorder(root_node.right)
    return


def print_postorder(root_node):
    """
     Given a root node, prints the postorder traversal of it.
     PostOrder Traversal:
         Left --> Right --> Root
     Use cases:
         Postfix mathematical operations
                                 2 9 *
         While deleting a tree, should follow this approach
    """
    if root_node:
        print_postorder(root_node.left)
        print_postorder(root_node.right)
        print('  {}  '.format(root_node.value))
    return

