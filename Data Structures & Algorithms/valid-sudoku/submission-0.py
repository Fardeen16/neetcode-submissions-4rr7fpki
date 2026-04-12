class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        #checking rows
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in rows[i] or
                board[i][j] in columns[j] or
                board[i][j] in squares[(i//3, j//3)]):
                    return False
                rows[i].add(board[i][j])
                columns[j].add(board[i][j]) 
                squares[(i//3,j//3)].add(board[i][j])
        return True



        #checking columns
        for i in range(0, 8):
            for j in board[i]:
                if board[j][i] not in columns[i] and board[j][i] != ".":
                    columns[i].append(board[j][i])
                else:
                    return False
        
        #checking the square
        

        
        