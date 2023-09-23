# from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        subset = set(words)
        g = defaultdict(list)

        for word in words:
            for j in range(len(word)):
                substring = word[:j] + word[j+1:]
                g[substring].append(word)
        
        
        
        def bfs(word):
            Q = deque()
            Q.append((word, 1))
            visited[word] = True
            maxcnt = 0
            while Q:
                word, cnt = Q.popleft()
                maxcnt = max(maxcnt, cnt)
                for nei in g[word]:
                    if visited[nei]:
                        continue
                    visited[nei] = True
                    Q.append((nei, cnt + 1))
            return maxcnt

        answer = 0
        for word in subset:
            visited = defaultdict(int)
            depth = bfs(word)
            answer = max(answer, depth)
        return answer
