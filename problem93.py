"""
Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.
"""
# COPIED

class Node():  
    def __init__(self, data):  
        self.data = data  
        self.left = None
        self.right = None
  

def largestBST(node): 
   # Returns size of the largest BST subtree  
   # in a Binary Tree (efficient version).  
      
    # Set the initial values for calling  
    # largestBSTUtil()  
    Min = [999999999999] # For minimum value in      
                         # right subtree  
    Max = [-999999999999] # For maximum value in  
                          # left subtree  
      
    max_size = [0] # For size of the largest BST  
    is_bst = [0] 
      
    largestBSTUtil(node, Min, Max,  
                         max_size, is_bst)  
      
    return max_size[0] 
  
def largestBSTUtil(node, min_ref, max_ref,  
                         max_size_ref, is_bst_ref): 
    # Base Case  
    if node == None: 
        is_bst_ref[0] = 1 # An empty tree is BST  
        return 0 # Size of the BST is 0  
    Min = 999999999999
    left_flag = False
    right_flag = False
    ls, rs = 0, 0
    max_ref[0] = -999999999999
    ls = largestBSTUtil(node.left, min_ref, max_ref,  
                           max_size_ref, is_bst_ref)  
    if is_bst_ref[0] == 1 and node.data > max_ref[0]:  
        left_flag = True
    Min = min_ref[0] 
    min_ref[0] = 999999999999
    rs = largestBSTUtil(node.right, min_ref, max_ref, 
                        max_size_ref, is_bst_ref)  
    if is_bst_ref[0] == 1 and node.data < min_ref[0]:  
        right_flag = True
    if Min < min_ref[0]:  
        min_ref[0] = Min
    if node.data < min_ref[0]: # For leaf nodes  
        min_ref[0] = node.data 
    if node.data > max_ref[0]:  
        max_ref[0] = node.data 
    if left_flag and right_flag: 
        if ls + rs + 1 > max_size_ref[0]:  
            max_size_ref[0] = ls + rs + 1
        return ls + rs + 1
    else: 
        return 0
  
# Driver Code 
if __name__ == '__main__': 
      
    # Let us construct the following Tree  
    #     50  
    # /     \  
    # 10     60  
    # / \     / \  
    # 5 20 55 70  
    #         /     / \  
    #     45     65 80 
    root = Node(50)  
    root.left     = Node(10)  
    root.right     = Node(60)  
    root.left.left = Node(5)  
    root.left.right = Node(20)  
    root.right.left = Node(55) 
    root.right.left.left = Node(45)  
    root.right.right = Node(70) 
    root.right.right.left = Node(65)  
    root.right.right.right = Node(80) 
  
# The complete tree is not BST as 45 is in  
# right subtree of 50. The following subtree 
# is the largest BST  
#     60  
# / \  
# 55     70  
# /     / \  
# 45     65 80  
  
print("Size of the largest BST is",  
                  largestBST(root))