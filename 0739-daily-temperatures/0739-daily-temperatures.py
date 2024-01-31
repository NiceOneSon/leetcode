class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]
        stack = [(temperatures[-1], len(temperatures)-1)]
        for i in range(len(temperatures)-2, -1, -1):
            cnt = 1
            while stack and stack[-1][0] <= temperatures[i]:
                cnt += 1
                stack.pop()
            if stack:
                answer.append(stack[-1][1] - i)
            else:
                answer.append(0)
            stack.append((temperatures[i], i))
        return answer[::-1]
        