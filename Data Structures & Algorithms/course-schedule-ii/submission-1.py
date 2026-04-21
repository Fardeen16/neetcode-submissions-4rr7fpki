class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}
        result = []

        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        visited = set()
        visiting = set()
        print(adj_list)
        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            
            visiting.add(node)
            for nei in adj_list[node]:
                if dfs(nei) == False:
                    return False
            #adj_list[node] = []
            visiting.remove(node)
            visited.add(node)
            result.append(node)
            return True


        for c in range(numCourses):
            if not dfs(c):
                return []
        return result
        