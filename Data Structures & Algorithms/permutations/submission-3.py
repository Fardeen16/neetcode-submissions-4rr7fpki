class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, sol = [], []
        visited = set()

        def backtrack(sett):
            if len(sol) == len(nums):
                ans.append(sol[:])
                return 
            
            for i in nums:
                if i not in sett:
                    sol.append(i)
                    sett.add(i)
                    backtrack(sett)
                    sol.pop()
                    sett.remove(i)
            
        backtrack(visited)
        return ans