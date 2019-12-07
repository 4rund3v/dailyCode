"""
Given a binary tree of integers, find the maximum path sum between two nodes.
 The path must go through at least one node, and does not need to go through the root.
"""

class Node():
    left = None
    right = None
    val = None


class Solution:
    #def maxPathSum(self, root) -> int:
    def maxPathSum(self, root):
        self.res = root.val
        # The max[n] means max path-sum with n as root.
        # The transfer equation is defined as:
        # max[n] = max(
        #   node.val
        #   max[n.left] + node.val,
        #   max[n.right] + node.val,
        #   max[n.right] + max[n.left] + node.val
        # )
        # Maximum of max[i] is the answer.
        def dfs(node):
            if not node:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            cur_max = max(
                node.val, 
                node.val + left_max, 
                node.val + right_max
            )
            self.res = max(self.res, cur_max, node.val + left_max + right_max)
            return cur_max
        dfs(root)
        return self.res
