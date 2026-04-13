class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [[grid[0][0], 0, 0]]  #[time, i, j]
        visited_set = set()
        #max_time = 1
        n = len(grid)
        visited_set.add((0, 0))

        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        while min_heap:
            time, i, j = heapq.heappop(min_heap)

            if i == n-1 and j == n-1:
                return time

            for dr, dc in directions:
                new_r, new_c = dr+i, dc+j
                if 0 <= new_r < n and 0 <= new_c < n and (new_r, new_c) not in visited_set:
                    
                    visited_set.add((new_r, new_c))
                    heapq.heappush(min_heap, (max(time, grid[new_r][new_c]), new_r, new_c))

        