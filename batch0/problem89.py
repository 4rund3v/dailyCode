"""
Determine whether a tree is a valid binary search tree.
A binary search tree is a tree with two children, left and right,
and satisfies the constraint that the key in the left child must be less than
or equal to the root and the key
in the right child must be greater than or equal to the root.
"""

class Node():
    left = None
    right = None
    val = 0


def solution(node):
    status = True
    def check_validity(node):
        global status
        if node.left:
            print(node.left.val, node.val)
            if node.left.val > node.val:
                status = False
                print('set to false !!')
            else:
                check_validity(node.left)
        if node.right:
            if node.right.val < node.val:
                status= False
            else:
                check_validity(node.right)
    check_validity(node)
    return status

if __name__ == "__main__":
    valid_bst = Node()
    valid_bst.val = 10
    lefty = Node()
    lefty.val = 5
    righty = Node()
    righty.val = 15
    valid_bst.left = lefty
    valid_bst.right = righty
    print('Valid bst validity is : {}'.format(solution(valid_bst)))
    invalid_bst = Node()
    invalid_bst.val = 10
    lefty = Node()
    lefty.val = 15
    righty = Node()
    righty.val = 5
    invalid_bst.left = lefty
    invalid_bst.right = righty
    print('InValid bst validity is : {}'.format(solution(invalid_bst)))
    #TODO not sure why status is not being updated.