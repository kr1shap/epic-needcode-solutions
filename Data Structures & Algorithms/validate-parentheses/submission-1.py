class Solution:
    def isValid(self, s: str) -> bool:
        matching = {"{": "}", "(": ")", "[": "]"}
        stack = []
        for char in s:
            if char in "})]":
                if len(stack)==0:
                    return False
                c = stack.pop()
                if matching[c] == char:
                    continue
                return False
            else:
                stack.append(char)
        return len(stack) ==0