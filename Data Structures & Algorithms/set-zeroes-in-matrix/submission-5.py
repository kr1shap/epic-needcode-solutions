class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    # set entire row and col to 'X' if not 0 
                    for col in range(0, len(matrix[0])):
                        if matrix[i][col] != 0 and matrix[i][col] != 'X': 
                            matrix[i][col] = 'X'
                    for row in range(0, len(matrix)):
                        if matrix[row][j] != 0 and matrix[row][j] != 'X': 
                            matrix[row][j] = 'X'
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'X':
                    matrix[i][j] = 0
        return 