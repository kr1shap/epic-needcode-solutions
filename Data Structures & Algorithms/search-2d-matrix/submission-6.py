class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do binary search on rows to find the row to search in 
        # do this by checking last index of lo, first index of hi 

        # binary search on row 
        lo = 0 
        hi = len(matrix)-1
        mid = 0
        while lo <= hi: 
            mid = (lo+hi)//2
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[0])-1]: 
                break #found 
            elif matrix[mid][0] > target: # go to lo row 
                hi = mid-1
            elif matrix[mid][len(matrix[0])-1] < target: # go to hi 
                lo = mid + 1
        if lo > hi: 
            return False

        # do binary search pt 2 
        bina = matrix[mid]
        lo = 0 
        hi = len(bina)-1
        while lo <= hi: 
            mid = (lo+hi)//2
            if bina[mid] == target: 
                return True
            elif bina[mid] > target: 
                hi = mid - 1
            else: 
                lo = mid + 1
        return False