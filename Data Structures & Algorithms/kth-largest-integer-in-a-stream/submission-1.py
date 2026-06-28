import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #self.storage = sorted(nums) if nums else []
        #self.pointer = k


        #min heap
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        #self.storage.append(val)
        #self.storage = sorted(self.storage)
        #return self.storage[-self.pointer]

        #min heap: O(log(k)) time through heappush, heappop
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

