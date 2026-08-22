class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        # parse through temperatures end to start 
        j = len(temperatures)-1
        while j >= 0: 
            val = temperatures[j]
            while len(stack) > 0:
                top = stack[-1]
                if temperatures[top] <= val: 
                    stack.pop()
                    continue
                else:
                    break   
            if len(stack) == 0: 
                res[j] = 0
            else: 
                res[j] = top - j
            stack.append(j)
            j-=1

        return res
        