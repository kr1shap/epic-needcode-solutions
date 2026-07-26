class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #preform binary search to get the right row 
        rowN = -1
        low = 0
        high = len(matrix)-1
        while low <= high:
            mid = (low+high)//2
            row = matrix[mid]
            #check if integer lies between the row 
            if row[0] <= target <= row[len(row)-1]:
                rowN = mid
                break
            #else, if target is less than 0th elemenent
            if target < row[0]:
                high = mid-1
            else:
                low = mid+1
        if rowN == -1: 
            return False
        #search in arr for target
        low = 0
        row = matrix[rowN]
        high = len(row)-1
        while low <= high: 
            mid = (low+high)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return False
