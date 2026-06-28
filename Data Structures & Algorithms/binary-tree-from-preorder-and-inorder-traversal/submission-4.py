# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder: node, left, right => first: root
        #inorder: left, node,   right => root splits the two halves
        #hashmap for O(1) lookup
        indices = {val:i for i, val in enumerate(inorder)}

        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
              return None
        
            root = TreeNode(preorder[pre_start])
            mid = indices[preorder[pre_start]]
            left_size = mid - in_start

            root.left = build(pre_start + 1, pre_start + left_size, in_start, mid-1)
            root.right = build(pre_start + left_size+1, pre_end, mid + 1, in_end)
        
            return root

        return build(0, len(preorder)-1, 0, len(inorder)-1)

3