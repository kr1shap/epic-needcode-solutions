class Solution:

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        # iterate from second last ele 
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
