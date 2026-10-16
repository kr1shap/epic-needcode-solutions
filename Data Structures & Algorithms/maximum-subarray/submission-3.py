class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        res = -193102909
        curSum = 0
        for r in range(len(nums)):
            curSum = max(curSum+nums[r], nums[r])
            res = max(res, curSum)
            # if nums[r]> nums[r]+curSum:
            #     res = max(res, nums[r])
            #     curSum = nums[r]
            # else:
            #     curSum += nums[r]
            #     res = max(res, curSum)       
        return res
