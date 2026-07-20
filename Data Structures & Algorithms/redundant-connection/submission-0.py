class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #union find
        n = len(edges)
        parent = list(range(n+1))

        def find(i):
            if parent[i] == i:
                return i
            
            parent[i] = find(parent[i])#path compression
            return parent[i]
        
        def union(i, j):
            r_i = find(i)
            r_j = find(j)
            if r_j == r_i:
                return False
            parent[r_i] = r_j
            return True
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]
          

