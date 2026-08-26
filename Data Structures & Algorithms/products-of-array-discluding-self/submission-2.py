class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix arrays 
        prefix = []
        suffix = [0 for i in range(0, len(nums))]
        for i in range(0, len(nums)):
            if i == 0: 
                prefix.append(1)
            else: 
                prefix.append(nums[i-1]*prefix[i-1])
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1: 
                suffix[i] = 1
            else:
                suffix[i] = (nums[i+1]*suffix[i+1])
        output = []
        for i in range(0, len(nums)):
            output.append(prefix[i]*suffix[i])
        return output