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
                rightHeights[len(height)-1] = 0
            else:
                maxL = max(height[i-1], maxL)
                leftHeights[i] = maxL
                maxR = max(height[len(height)-i], maxR)
                rightHeights[len(height)-1-i] = maxR
        water = 0 
        for i in range(len(height)):
            if i == 0 or i == len(height)-1: 
                continue
            leftH = leftHeights[i]
            rightH = rightHeights[i]
            h = min(leftH, rightH)
            area = h-height[i]
            if area > 0: 
                water+=area
        return water