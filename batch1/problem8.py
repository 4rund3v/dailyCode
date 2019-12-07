'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

class Node():
    left = None
    right = None
    data = None


def solution(root_node):
    global count
    def check_unival(node):
        global count
        if node.left == node.right == None:
            # leaf node case
            count += 1
        if node.left:
            if node.left and not node.right:
                # if the left node exists only and its parent has same value
                if node.data == node.left.data:
                    count += 1
            check_unival(node.left)            
        if node.right:
            if node.right and not node.left:
                # if the right node exists only and its parent has same value
                if node.data == node.right.data:
                    count += 1
            check_unival(node.right)            
        if node.left and node.right:
            if node.left.data == node.right.data == node.data:
                # if the node and its children all have same value.
                count += 1                
    check_unival(root_node)
    return count


if __name__ == "__main__":
    root_node = Node()
    c1 = Node()
    c2 = Node()
    c3 = Node()
    c4 = Node()
    c5 = Node()
    c6 = Node()
    root_node.data = 0
    c1.data = 1
    c2.data = 0
    c3.data = 1
    c4.data = 0
    c5.data = 1
    c6.data = 1
    root_node.left = c1
    root_node.right = c2
    c2.left = c3
    c2.right = c4
    c3.left = c5
    c3.right = c6
    count = 0
    print(solution(root_node))
