class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        visited_set = set()
        def dfs(node):
            if adj_list[node] == []:
                return True
            if node in visited_set:
                return False
            
            visited_set.add(node)
            for nei in adj_list[node]:
                if not dfs(nei):
                    return False
            adj_list[node] = []
            visited_set.remove(node)
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        