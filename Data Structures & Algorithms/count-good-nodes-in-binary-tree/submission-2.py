# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:      

        def traverse(node, maximum):
            if not node:
                return 0

            count = 1 if node.val >= maximum else 0
            maximum = max(maximum, node.val)     

            count += traverse(node.left, maximum)
            count += traverse(node.right, maximum)

            return count

        return traverse(root, root.val)

        
