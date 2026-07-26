class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        #prefix and suffix multipliers 
        prefixMultipliers = [1]*len(nums) #length nums
        suffixMultipliers = [1]*len(nums)
        #obtain prefix and suffix multipliers
        for i in range(len(nums)): #prefix
            if i == 0:
                prefixMultipliers[i] = 1
                continue
            prefixMultipliers[i]=prefixMultipliers[i-1]*nums[i-1]
        for i in range(len(nums)-1, -1, -1): #suffix
            if i == len(nums)-1:
                suffixMultipliers[i] = 1
                continue
            suffixMultipliers[i]=suffixMultipliers[i+1]*nums[i+1]
        #get the result
        for i in range(len(nums)):
            output.append(prefixMultipliers[i]*suffixMultipliers[i])
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # #get prefix products 
        # prefix=[0]*len(nums)
        # suffix=[0]*len(nums)
        # for i in range(0, len(nums)):
        #     if i == 0:
        #         prefix[i] = 1
        #     else:
        #         prefix[i] = prefix[i-1]*nums[i-1]
        # #get suffix products
        # for i in range(len(nums)-1, -1, -1):
        #     if i == len(nums)-1: 
        #         suffix[i] = 1
        #     else:
        #         suffix[i] = suffix[i+1]*nums[i+1]
        # #create res
        # print(prefix)
        # print(suffix)
        # res = []
        # for i in range(len(nums)):
        #     res.append(suffix[i]*prefix[i])
        # return res