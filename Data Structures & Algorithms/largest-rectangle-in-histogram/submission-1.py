class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftRes = [ 0 for _ in range(len(heights))]
        rightRes = [ 0 for _ in range(len(heights))]

        st = [] # ( val, idx )

        for i in range(len(heights)):
            # left pass stack
            while st and st[-1][0] >= heights[i]:
                st.pop()
            if st:
                leftRes[i] = st[-1][1]
            else: 
                leftRes[i] = -1
            st.append((heights[i], i)) 
        st = []
        for i in range(len(heights)-1, -1, -1):
            # right pass stack
            while st and st[-1][0] >= heights[i]:
                st.pop()
            if st:
                rightRes[i] = st[-1][1]
            else: 
                rightRes[i] = len(heights)
            st.append((heights[i], i)) 

        # compute result 
        res = 0 
        for i in range(len(heights)):
            left = leftRes[i]
            right = rightRes[i]
            res = max(res, heights[i]*(right-left-1))
        return res
