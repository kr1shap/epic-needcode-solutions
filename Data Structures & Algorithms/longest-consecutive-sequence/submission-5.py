class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums) #get set of all numbers for easy lookup
        maxLength = 0
        for n in nums:
            if n-1 not in uniqueNums: #start of sequence
                currentLength = 1
                while n+1 in uniqueNums:
                    currentLength+=1
                    n+=1
                maxLength = max(maxLength, currentLength)
        return maxLength