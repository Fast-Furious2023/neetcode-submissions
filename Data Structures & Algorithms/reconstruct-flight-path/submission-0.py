from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for source, destination in tickets:
            adj[source].append(destination)

        for src in adj:
            adj[src].sort(reverse=True)

        itinerary = []

        def dfs(airport):

            while adj[airport]:
                next_airport = adj[airport].pop()#the lexically smallest
                dfs(next_airport)

            itinerary.append(airport)
        
        dfs("JFK")

        return itinerary[::-1]


            

