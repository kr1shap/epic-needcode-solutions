class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        L = 0 
        R = len(matrix)-1
        while L < R: 
            for i in range(R-L):
                # top left 
                topL = matrix[L][L+i]
                topR = matrix[L+i][R]
                # bottom 
                bottomL = matrix[R][R-i]
                bottomR = matrix[R-i][L]

                #swap them 
                matrix[L][L+i] = bottomR
                matrix[L+i][R] = topL
                matrix[R][R-i] = topR
                matrix[R-i][L] = bottomL
                
            L+=1
            R-=1



