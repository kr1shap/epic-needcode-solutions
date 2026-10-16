class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)-1, -1, -1):
            while st and st[-1][0] <= temperatures[i]:
                st.pop()
            if st: 
                res[i] = st[-1][1]-i
            else:
                res[i] = 0
            st.append((temperatures[i], i))
        return res
