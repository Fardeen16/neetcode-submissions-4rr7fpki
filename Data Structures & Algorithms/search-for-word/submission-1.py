class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        n = len(word)

        if r == 1 and c == 1:
            return board[0][0] == word

        def backtrack(i, j, index):
            if n == index:
                return True

            if board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = "*"            
            for dr, dc in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                next_i, next_j = i + dr, j + dc
                if 0 <= next_i < r and 0 <= next_j < c:
                    if backtrack(next_i, next_j, index + 1):
                        return True
                    
            board[i][j] = temp
            return False
        
        for i in range(r):
            for j in range(c):
                if backtrack(i, j, 0):
                    return True
        return False

        