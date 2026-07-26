class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue #skip repeats to check sums for 
            #now iterate through i+1 -> len(nums)
            j = i + 1
            k = len(nums)-1
            while j < k:
                s = nums[j] + nums[k] + nums[i]
                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                elif s > 0: #need more negative
                    #move k pointer to lower s 
                    k-=1
                else:
                    j+=1
                
                #now move the j and k pointer until we hit a new number
        return res