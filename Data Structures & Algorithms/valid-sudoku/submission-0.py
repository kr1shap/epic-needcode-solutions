class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #iterate through row 
        for row in board:
            curr = set()
            for num in row:
                if num in curr:
                    return False
                elif num != ".":
                    curr.add(num)
        #Iterate through col 
        for j in range(len(board[0])):
            curr = set()
            for i in range(len(board)):
                if board[i][j] in curr:
                    return False
                elif board[i][j] != ".":
                    curr.add(board[i][j])
        #iterate through all 3x3 
        groups = len(board)/3
        for gp in range(int(groups*groups)):
            #iterate row by row of 3x3 blocks
            curr = set()
            for i in range(3):
                for j in range(3):
                    row = (gp//3)*3+i
                    col = (gp%3)*3+j
                    if board[row][col] in curr:
                        return False
                    elif board[row][col] != ".":
                        curr.add(board[row][col])
        return True


                