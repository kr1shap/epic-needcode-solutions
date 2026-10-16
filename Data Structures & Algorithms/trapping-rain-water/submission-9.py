class Solution:
    def trap(self, height: List[int]) -> int:
        # compute max for left and right 
        leftM = [float("inf") for _ in range(len(height))]
        rightM = [float("inf") for _ in range(len(height))]
        for i in range(1, len(height)-1):
            if i == 1:
                leftM[i] = height[0]
                continue
            leftM[i] = max(leftM[i-1], height[i-1])
        for i in range(len(height)-2, 0, -1):
            if i == len(height)-2:
                rightM[i] = height[len(height)-1]
                continue
            rightM[i] = max(rightM[i+1], height[i+1])
    
        water = 0
        for i in range(1, len(height)-1):
            water += max(0, min(leftM[i], rightM[i])-height[i])
        return water
