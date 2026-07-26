class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #get prefix products 
        prefix=[0]*len(nums)
        suffix=[0]*len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = prefix[i-1]*nums[i-1]
        #get suffix products
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1: 
                suffix[i] = 1
            else:
                suffix[i] = suffix[i+1]*nums[i+1]
        #create res
        print(prefix)
        print(suffix)
        res = []
        for i in range(len(nums)):
            res.append(suffix[i]*prefix[i])
        return res