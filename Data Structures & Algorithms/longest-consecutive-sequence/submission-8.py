class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        seen = set()
        length = 0 
        maxLength = 0 
        for i in range(len(nums)):
            if i == 0: 
                length+=1
            elif nums[i] in seen: 
                continue
            elif nums[i]-1 not in seen: 
                maxLength = max(maxLength, length)
                length = 1 
            else: 
                length+=1
            seen.add(nums[i])
        return max(length, maxLength)

[-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]
