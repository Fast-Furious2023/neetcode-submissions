import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        #small heap should be smaller than large heap
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large,-heapq.heappop(self.small))
        #main size balance
        if len(self.small) > len(self.large)+1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small)+1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return float(-self.small[0])
        elif len(self.small)<len(self.large):
            return float(self.large[0])
        else:
            return (self.large[0] - self.small[0])/2.0
        
        