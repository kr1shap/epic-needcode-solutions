class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotate has two cases
        # left < mid < hi -> go hi = mid - 1 
        # mid < hi < left -> 
        lo = 0 
        hi = len(nums)-1
        mid = (lo+hi)//2
        while lo <= hi: 
            mid = (lo+hi)//2
            l = nums[lo]
            h = nums[hi]
            m = nums[mid]
            if l <= m <= h: 
                return l
            elif m <= h <= l: 
                hi = mid
            elif h <= l <= m: 
                lo = mid+1
        return nums[mid]