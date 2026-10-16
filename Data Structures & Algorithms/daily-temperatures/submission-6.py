class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)-1, -1, -1):
            temp = temperatures[i]
            if not st: 
                st.append((temp, i))
                res[i] = 0
                continue
            else: 
                while st and st[-1][0] <= temp: 
                    st.pop()
                if not st: 
                    res[i] = 0
                else: 
                    res[i] = st[-1][1] - i
                st.append((temp, i))
        return res
