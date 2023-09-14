class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        routes = defaultdict(list)
        
        for f, t in sorted(tickets, reverse = True):
            routes[f].append(t)
        
        answer = []
        def dfs(airport):
            while routes[airport]:
                target = routes[airport].pop()
                dfs(target)
                answer.append(target)
                
            
        dfs("JFK")
        answer.append("JFK")
        
        return answer[::-1]