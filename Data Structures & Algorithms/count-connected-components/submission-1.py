class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        count = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj_list[node]:
                dfs(nei)
            
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
            else:
                continue
        
        return count 
        

        