# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # longest path through a node: leftchild's + right's + 2
        self.diameter = 0
        def height(node):
            if not node:
                return 0
            
            h_left = height(node.left)
            h_right = height(node.right)
            self.diameter = max(self.diameter, h_left + h_right)
            return max(h_left, h_right) + 1
        height(root)

        return self.diameter