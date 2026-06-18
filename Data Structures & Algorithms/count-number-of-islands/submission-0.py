class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited_set = set()
        islands = [0]

        def dfs(i, j):
            if (i, j) in visited_set:
                return

            visited_set.add((i, j))

            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                r, c = dr+i, dc+j
                if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == "1":
                    dfs(r, c)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited_set:
                    islands[0] += 1
                    dfs(i, j)
        
        return islands[0]

        