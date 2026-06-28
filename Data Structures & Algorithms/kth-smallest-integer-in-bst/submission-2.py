# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #in-order traversal of BST=> ascendigng order 
        self.counter=0
        self.curr=-1
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
         
            self.counter+=1
            if self.counter == k:
                self.curr = node.val
                return 
            if self.counter < k:
                 traverse(node.right)

        traverse(root)
        return self.curr