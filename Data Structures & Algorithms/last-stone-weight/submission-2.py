import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #return last remaining stone or 0 if none remains
        stones = [-e for e in stones]
        heapq.heapify(stones)
        heap = stones
        while heap and len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x > y:
                heapq.heappush(heap, -(x-y))
        
        if not heap:
            return 0
        else:
            return -heap[0]
     


        