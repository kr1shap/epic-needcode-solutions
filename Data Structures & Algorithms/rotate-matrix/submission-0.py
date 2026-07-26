class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #create transpose 
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        #reverse all rows
        for row in matrix:
            row.reverse()
        