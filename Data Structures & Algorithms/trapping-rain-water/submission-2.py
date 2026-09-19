class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        leftHeights = [0 for _ in range(len(height))]
        rightHeights = [0 for _ in range(len(height))]
        maxL = -1
        maxR = -1
        for i in range(len(height)):
            if i == 0: 
                leftHeights[i] = 0
                continue
            else:
                maxL = max(height[i-1], maxL)
                leftHeights[i] = maxL
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                rightHeights[i] = 0
                continue
            else: 
                maxR = max(height[i+1], maxR)
                rightHeights[i] = maxR
        # compute 
        water = 0 
        for i in range(len(height)):
            if i == 0 or i == len(height)-1: 
                continue
            leftH = leftHeights[i]
            rightH = rightHeights[i]
            h = min(leftH, rightH)
            area = h-height[i]
            if area >=0: 
                water+=area
        return water