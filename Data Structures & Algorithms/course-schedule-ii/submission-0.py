from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:set() for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        for course, pre in prerequisites:
            adj[pre].add(course)
            indegree[course]+=1
        
        queue=deque([c for c in indegree if indegree[c] ==0])
        res = []

        while queue:
            completed = queue.popleft()

            res.append(completed)

            for neighbors in adj[completed]:
                indegree[neighbors]-=1
                if indegree[neighbors]==0:
                    queue.append(neighbors)

        if len(res)<len(indegree):
            return[]
        
        return res