from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #return minimum number of CPU cycles

        #execute the most frequent tasks first, by using a max-heap(negate)
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        queue = deque()
        time = 0

        while heap or queue:
            time += 1

            if heap:
                freq = heapq.heappop(heap) + 1
                if freq != 0:
                    queue.append([freq,time + n])
            
            if queue and time == queue[0][1]:
                heapq.heappush(heap, queue[0][0])
                queue.popleft()
               
        return time





        #use a queue to track the cooldown time 
        