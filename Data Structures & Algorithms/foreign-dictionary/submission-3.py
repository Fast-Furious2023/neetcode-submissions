from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #get all unique characters, create adjacency list for every char and indegree map 
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for w in words for c in w}

        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            min_len = min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:min_len] == w2:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    c1,c2=w1[j],w2[j]
                    

                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2]+=1

                    break


        #use a queue to sort the chars/topological sort
        queue = deque([c for c in indegree if indegree[c]==0])
        res = []

        while queue:
            char = queue.popleft()
            res.append(char)
            for e in adj[char]:
                indegree[e]-=1
                if indegree[e]==0:
                    queue.append(e)
        
        if len(res) < len(indegree):
            return ""

        return "".join(res)


        
