class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find minimum first 
        low = 0
        high = len(nums)-1
        breakPoint = 0
        while low<=high: 
            mid = (low+high)//2
            if nums[low] <= nums[mid] <= nums[high]:
                breakPoint = low #this is the index of lowest ele
                break
            elif nums[high] <= nums[low] <= nums[mid]:
                low = mid+1
            else:
                high = mid

        #after finding breakpoint, we search in two arrays
        arr1 = nums[breakPoint:]
        arr2 = nums[0:breakPoint]
        rightArr = []
        if len(arr1) != 0 and target <= arr1[len(arr1)-1]:
            rightArr = arr1
        else:
            rightArr = arr2
        #preform binary in array
        low = 0
        high = len(rightArr)-1
        print(rightArr)
        while low<=high:
            mid = (low+high)//2
            if rightArr[mid]==target and rightArr == arr2:
                return mid
            if rightArr[mid]==target and rightArr == arr1:
                return mid+breakPoint
            elif rightArr[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1