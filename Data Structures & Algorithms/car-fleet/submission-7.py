from collections import defaultdict
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []

        # hashmap of position to speed
        pos_to_speed = defaultdict(int)
        for i in range(len(position)):
            pos_to_speed[position[i]] = speed[i]

        # sort positions 
        position.sort(reverse=True)
        count = 0
        # traverse 
        for i in range(len(position)):
            pos = position[i]
            endTime = float((target - pos) / pos_to_speed[pos])
            if not st or st[-1][1] < endTime: 
                st.append((pos, endTime))
        return len(st)
            
