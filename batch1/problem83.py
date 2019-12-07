"""
Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""

class Node():
    left = None
    right = None
    val = None

def swap_nodes(node):
    if node:
        if node.left:
            swap_nodes(node.left)
        if node.right:
            swap_nodes(node.right)
        node.left, node.right = node.right, node.left
    
if __name__ == "__main__":
    root_node = Node()
    root_node.val = 'a'
    bnode = Node( )
    bnode.val = 'b'
    cnode = Node()
    cnode.val = 'c'
    dnode = Node()
    dnode.val = 'd'
    enode = Node()
    enode.val = 'e'
    fnode = Node()
    fnode.val = 'f'
    root_node.left = bnode
    root_node.right = cnode   
    bnode.left = dnode
    bnode.right = enode
    cnode.left = fnode

    swap_nodes(root_node)
    print(root_node.val)
    print('left of root is : {}'.format(root_node.left.val))
    print('right of root is : {}'.format(root_node.right.val))
