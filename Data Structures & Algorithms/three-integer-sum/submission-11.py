class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()
        # compute j + k = -i 
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 2 ptr 2-sum 
            l = i + 1 
            r = len(nums)-1
            while l < r: 
                res = nums[l] + nums[r]
                if res == -nums[i]: 
                    final.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l-1] == nums[l]: 
                        l+=1
                    while l < r and nums[r+1] == nums[r]: 
                        r-=1
                elif res > -nums[i]:
                    r-=1
                else:
                    l+=1
                
        return final
                