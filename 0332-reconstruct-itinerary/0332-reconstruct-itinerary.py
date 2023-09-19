class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        routes = defaultdict(list)
        for k, v in sorted(tickets, reverse = True):
            routes[k].append(v)
        
        
        answer = []
        def dfs(k):
            while routes[k]:
                v = routes[k].pop()
                dfs(v)
                answer.append(v)
        
        dfs("JFK")
        answer.append("JFK")
        
        return answer[::-1]