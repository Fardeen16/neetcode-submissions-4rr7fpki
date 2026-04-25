class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        firstRow = False 

        # first we find and store all zeros in 1st column and 1st row
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        firstRow = True
        
        # now we iterate to change all possible positions to zero
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # now we zero any remaining 1s left
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if firstRow:
            for c in range(COLS):
                matrix[0][c] = 0
         
        

        
        