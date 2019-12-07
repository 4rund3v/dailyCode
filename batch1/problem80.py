"""
Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
"""

class Node():
    left = None
    right = None
    data = None

def solution(root_node):
    depth_map = {}
    def deepest_node(source_node, depth):
        if not depth_map.get(depth):
            depth_map[depth] = set()
        depth_map[depth].add(source_node.data)
        if source_node.left:
            deepest_node(source_node.left, depth+1)
        if source_node.right:
            deepest_node(source_node.right, depth+1)
        return depth
    deepest_node(root_node, 0)
    return depth_map


if __name__ == "__main__":
    root_node = Node()
    node_b = Node()
    node_c = Node() 
    node_d = Node()
    root_node.data = 'a'
    node_b.data = 'b'
    node_c.data = 'c'
    node_d.data = 'd'
    root_node.left = node_b
    root_node.right = node_c
    node_b.left = node_d
    sol = solution(root_node)
    print('max depth is : {}'.format(sol[max(sol)]))
