class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maxW =0
        while i < j:
            water = min(heights[i], heights[j])*(j-i)
            maxW = water if water > maxW else maxW
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return maxW