class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def rec(index: int, arr: List[int]) -> None: 
            if index >= len(nums):
                res.append(arr[:])
                return
            arr2 = arr.copy()
            rec(index + 1, arr2 + [nums[index]])
            # where we exclude curr num
            for i in range(index+1, len(nums)):
                if nums[index] == nums[i]:
                    continue
                else: 
                    rec(i, arr2[:])
                    return
            rec(len(nums), arr2[:])
                
        
        rec(0, [])
        return res