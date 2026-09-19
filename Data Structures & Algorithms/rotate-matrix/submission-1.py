class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        L = 0
        R = len(matrix)-1 
        layer = 0 
        while L < R: 
            for i in range(R-L):
                top = matrix[L][L+i] #shifts right 
                bottom = matrix[R][R-i] #shifts left 

                left = matrix[R-i][L] #shifts top 
                right = matrix[L+i][R] #shifts bottom 

                # right becomes top 
                # bottom becomes right 
                # left becomes bottom 
                # top becomes left 
                matrix[L][L+i] = left 
                matrix[R][R-i] = right
                matrix[R-i][L] = bottom 
                matrix[L+i][R] = top
            L+=1
            R-=1
        

