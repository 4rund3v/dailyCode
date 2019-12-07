#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""

class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None



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
