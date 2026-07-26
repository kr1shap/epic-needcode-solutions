class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        dic = {}
        if len(nums) == 0: 
            return 0
        for num in numSet:
            if num-1 not in dic: 
                dic[num] = 1
                while (num+dic[num]) in numSet: 
                    dic[num]+=1
        return max(dic.values())