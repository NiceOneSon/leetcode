class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        result = 0

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                result += arr[mid] * (mid - left) * (right - mid)
                result %= MOD
            stack.append(i)

        # Handle remaining elements in the stack
        while stack:
            mid = stack.pop()
            left = stack[-1] if stack else -1
            right = n
            result += arr[mid] * (mid - left) * (right - mid)
            result %= MOD

        return result