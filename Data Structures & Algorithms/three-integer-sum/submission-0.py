class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    #combination of twosum problem and dp problem 
        nums.sort()
        res = []
        print("sorted nums, ", nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k: 
                # i + j + k = 0 -> i = -(j+k)
                if nums[i] +nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif nums[i] + nums[j] + nums[k] > 0: #too high, move r
                    k-=1
                else:
                    j+=1
        return res