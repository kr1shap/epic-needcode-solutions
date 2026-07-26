class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroRow = False
        zeroCol = False
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        zeroRow = True
                    if j == 0:
                        zeroCol = True
                    if i == 0 and j == 0:
                        continue
                    matrix[i][0] = "*" #row
                    matrix[0][j] = "*" #col
        print(matrix)
        #iterate through row 0 and zero out row 
        for i in range(0, len(matrix)):
            if i == 0: #do at end
                continue
            if matrix[i][0] == "*":
                #iterate and clear out 
                matrix[i] = [0 for k in range(len(matrix[0]))]
        #iterate through col 0 and zero out col 
        for i in range(0, len(matrix[0])):
            if i == 0: #do at end
                continue
            if matrix[0][i] == "*":
                #iterate and clear out 
                for j in range(len(matrix)):
                    matrix[j][i] = 0
        if zeroRow:
            matrix[0] = [0 for k in range(len(matrix[0]))]
        if zeroCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        