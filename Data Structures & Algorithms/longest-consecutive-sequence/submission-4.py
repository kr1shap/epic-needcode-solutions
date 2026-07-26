class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxS = 0
        for i in range(len(nums)):
            if nums[i]-1 not in s: 
                #iterate and find longest sequence
                temp=1
                while nums[i]+temp in s: 
                    temp+=1
                maxS = temp if temp > maxS else maxS
        return maxS
