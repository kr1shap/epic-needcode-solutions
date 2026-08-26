class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        arrLeft = [0 for i in range(0, len(heights))]
        arrRight = [0 for i in range(0, len(heights))]

        # do the left 
        stack = []
        for i in range(0, len(heights)):
            while stack and heights[stack[-1]] >= heights[i]: 
                stack.pop(-1)
            arrLeft[i] = 0 if len(stack) == 0 else stack[-1]+1
            stack.append(i)
        
        # do the right 
        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]: 
                stack.pop(-1)
            arrRight[i] = len(heights)-1 if len(stack) == 0 else stack[-1]-1
            stack.append(i)
        
        #compute 
        # formula = (right-left+1)*height 
        maxheight = -1
        for i in range(0, len(heights)):
            left = arrLeft[i]
            right = arrRight[i]
            maxheight = max(maxheight, (right-left+1)*heights[i])
        return maxheight

