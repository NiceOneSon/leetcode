class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        starting_points = [0] * numCourses

        for wannaget, required in prerequisites:
            graph[wannaget].append(required)
            starting_points[required] += 1

        q = deque([])

        for node, value in enumerate(starting_points):
            if value == 0:
                q.append(node)


        courseSequence=[]
        while q:
            startnode = q.popleft()
            courseSequence.append(startnode)    

            for next in graph[startnode]:
                starting_points[next] -= 1
                if starting_points[next] == 0:
                    q.append(next)
        return len(courseSequence) == numCourses