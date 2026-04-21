class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        total_fresh = [0]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    total_fresh[0] += 1
        print(total_fresh)

        visited_set = set()

        for r, c in q:
            visited_set.add((r, c))
        
        time = 0

        def dfs(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                
                grid[r][c] = 2
                q.append((r, c))
                total_fresh[0] -= 1
            else:
                return 

        while q and total_fresh[0] > 0:
            print(q)
            print(time)
            
            lenq = len(q)
            for i in range(lenq):
                r, c = q.popleft()
                
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
                #total_fresh -= 1
            time += 1
            print(total_fresh)
        return time if total_fresh[0] == 0 else -1

        