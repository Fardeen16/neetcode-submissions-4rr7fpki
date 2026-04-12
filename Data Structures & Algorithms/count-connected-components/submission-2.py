class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        
        def union(arr, a, b):
            root_a = find(arr, a)
            root_b = find(arr, b)

            if root_a == root_b:
                return
            arr[root_b] = root_a

        def find(arr, node):
            if arr[node] == node:
                return node
            return find(arr, arr[node])

        arr = [i for i in range(n)]

        for a, b in edges:
            union(arr, a, b)
        
        count = 0
        for i in range(len(arr)):
            if i == arr[i]:
                count += 1

        return count
            


























        # adj_list = defaultdict(list)
        # for a, b in edges:
        #     adj_list[a].append(b)
        #     adj_list[b].append(a)

        # count = 0
        # visited = set()

        # def dfs(node):
        #     if node in visited:
        #         return
        #     visited.add(node)
        #     for nei in adj_list[node]:
        #         dfs(nei)
            
        
        # for i in range(n):
        #     if i not in visited:
        #         count += 1
        #         dfs(i)
        #     else:
        #         continue
        
        # return count 
        

        