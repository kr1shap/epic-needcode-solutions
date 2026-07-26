class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            if target-nums[i] in sums:
                return [sums[target-nums[i]][0], i]
            if nums[i] not in sums:
                sums[nums[i]] = [i]
            else:
                sums[nums[i]].append(i)
        return []