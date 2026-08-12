class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}

        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(s1_index, s2_index):
            if (s1_index, s2_index) in cache:
                return cache[(s1_index, s2_index)]
            if s1_index == len(s1) and s2_index == len(s2):
                return True
            if s1_index < len(s1) and s1[s1_index] == s3[s1_index + s2_index] and dfs(s1_index+1, s2_index):
                return True
            
            if s2_index < len(s2) and s2[s2_index] == s3[s1_index + s2_index] and dfs(s1_index, s2_index + 1):
                return True
            
            cache[(s1_index, s2_index)] = False
            return False
        
        return dfs(0, 0)