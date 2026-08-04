class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        neg_diag = set()
        pos_diag = set()
        cols = set()
        ans = []

        board = [["."] * n for i in range(n)]

        def place_queen(r):
            if r== n:
                copy = ["".join(rows) for rows in board]
                ans.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c] = 'Q' 

                place_queen(r + 1)

                cols.remove(c)
                neg_diag.remove(r-c)
                pos_diag.remove(r+c)
                board[r][c] = '.'
        
        place_queen(0)
        return ans
        