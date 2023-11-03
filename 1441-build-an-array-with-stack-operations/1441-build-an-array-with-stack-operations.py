class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        curr = 1
        stack = []
        for number in target:
            if number == curr:
                stack.append("Push")
                curr += 1
            else:
                while curr < number:
                    stack.append("Push")
                    stack.append("Pop")
                    curr += 1
                stack.append("Push")
                curr += 1
        return stack