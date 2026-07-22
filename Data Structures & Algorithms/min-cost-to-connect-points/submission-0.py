import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #PLAN:
        #to build minimum spanning tree
        #use a boolean array to track the nodes in the tree
        #use a min-heap to find the closest node to the current tree
        
        #verify input
        n = len(points)
        if n <= 1:
            return 0

        #boolean array to track the current tree
        current_tree=[False]*n
        size_tree = 0

        #initialize min heap
        min_heap=[(0,0)] # (cost,node_i)
        total_cost = 0

        while min_heap and size_tree < n:
            cost, u = heapq.heappop(min_heap)
            
            if current_tree[u]:
                continue
                
            current_tree[u] = True
            size_tree += 1
            total_cost += cost

            for i in range(n):
                if not current_tree[i]:
                    dist = abs(points[u][0]-points[i][0]) + abs(points[u][1]-points[i][1])
                    heapq.heappush(min_heap,(dist,i))

        return total_cost


        

        