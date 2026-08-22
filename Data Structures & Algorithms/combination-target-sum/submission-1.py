class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def rec(target: int, index: int, arr: List[int]) -> Void: 
            if target == 0:
                res.append(arr) 
                return
            if index >= len(nums):
                return
            for i in range(index, len(nums)): 
                remaining = target - nums[i]
                if remaining >= 0: 
                    arr2 = arr[:]
                    arr2.append(nums[i])
                    rec(remaining, i, arr2[:])
                else: 
                    continue

        for i in range(0, len(nums)):
            rec(target-nums[i], i, [nums[i]])
        return res
         

        