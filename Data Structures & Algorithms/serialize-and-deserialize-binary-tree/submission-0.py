# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        res = []
        def dfs(root):
            nonlocal res 
            curr = root
            if not curr:
                res.append('N')
                return

            res.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)
        dfs(root)
        return ','.join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
       

        data = data.split(',')
        cursor = 0

        def dfs():
            nonlocal cursor
            
            if data[cursor] == 'N':
                cursor += 1
                return None
            
            node = TreeNode(int(data[cursor]))
            cursor += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
            
            



