class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def rec(target: int, nums: List[int], arr: List[int]) -> Void: 
            if target == 0 or len(nums) == 0:
                res.append(arr) 
                return
            for i in range(0, len(nums)): 
                remaining = target - nums[i]
                # print("arr = ", arr)
                # print("target = " ,target)
                # print("val of nums[i]:" ,nums[i], " remaining: ", remaining)
                if remaining >= 0: 
                    arr2 = arr[:]
                    arr2.append(nums[i])
                    rec(remaining, nums[i:], arr2[:])
                else: 
                    continue

        for i in range(0, len(nums)):
            rec(target-nums[i], nums[i:], [nums[i]])
        return res
         

        