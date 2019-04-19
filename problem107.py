"""
Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""


class Node():
    left = None
    right = None
    data =  None

def solution(root_node):
    # print in level order
    # each root followed by the left, right child
    def print_elements(node, root=False):
        if root:
            print(node.data)
        if node.left:
            print(node.left.data)
        if node.right:
            print(node.right.data)
        if node.left:
            print_elements(node.left)
        if node.right:
            print_elements(node.right)
    print_elements(root_node, root=True)


if __name__ == "__main__":
    root = Node()
    node_1 = Node()
    node_2 = Node()
    node_3 = Node()
    node_4 = Node()
    node_5 = Node()
    root.data = 1
    root.left = node_1
    root.right = node_2
    node_1.data = 2
    node_2.data = 3
    node_2.left = node_3
    node_2.right = node_4
    node_3.data = 4
    node_4.data = 5
    solution(root)
