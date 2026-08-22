class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(arr: List[int]) -> None: 
            if len(arr) == len(nums):
                res.append(arr)
                return
            for i in range(0, len(nums)):
                if nums[i] not in arr: 
                    arr2 = arr[:]
                    arr2.append(nums[i])
                    rec(arr2)
        rec([])
        return res
            

          
