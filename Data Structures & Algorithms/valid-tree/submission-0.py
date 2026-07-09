class UnionFind:
    def __init__(self,size):
        self.parent=[i for i in range(size)] #every elment points to itself
        self.count = size

    def find(self,i):#return the root of i
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        self.parent[root_x]=root_y
        self.count -= 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #two requirements for a graph to be a valid tree:
        #1.connected/one component
        #2. acyclic 

        if len(edges) != n-1:
            return False

        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u,v):
                return False
        return uf.count == 1
        

