"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #clone current node and its neighbors recusively
        #use a hash table to avoid loop

        visited = {}

        def dfs(node):
            if not node:
                return

            curr = node
            if curr in visited:
                return visited[curr]
            
            #clone the current node, and map it to the curr in visted
            cloned = Node(curr.val)
            visited[curr]=cloned

            #recursively clone curr's neighbors
            for neighbor in curr.neighbors:
                cloned.neighbors.append(dfs(neighbor))
            return cloned
        return dfs(node)

