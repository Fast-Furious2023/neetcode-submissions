from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #bfs
        #create a graph, if cycle exists, false
        #build adj list
        adj_list = {i:[] for i in range(numCourses)}
        #build in-degree array to store num of prerequisites
        in_degree = [0]*numCourses

        for des,src in prerequisites:
            adj_list[src].append(des) #src is prerequisite
            in_degree[des] += 1

        #use a counter for courses with no prerequisites left
        counter = 0

        #dfs: build a queue of courses with no prerequisites left
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while queue:
            curr = queue.popleft()
            counter += 1

            for neighbor in adj_list[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        


        #compare counter with numCourses, if equal-->true
        return counter == numCourses
