class Solution:
    def findMin(self, nums: List[int]) -> int:
        #preform binary search
        low = 0
        high = len(nums)-1
        while low <= high:
            print("low", low)
            print("high", high)
            mid = (low+high)//2
            if nums[low] <= nums[mid] <= nums[high]:
                #preform regular binary search
                return nums[low]
            elif nums[high] <= nums[low] <= nums[mid]:
                low = mid+1
            else:
                high = mid
        return nums[mid]