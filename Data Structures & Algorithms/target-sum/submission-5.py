class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        BF = O(2^n)

        optimal: 
        '''
        ways = [0]
        #total = [0]
        cache = {}  # {(index,sum) : ways}
        
        def dfs(index, total):
            if (index, total) in cache:
                return cache[(index, total)]

            if index == len(nums): 
                return 1 if total == target else 0
            
            cache[(index, total)] = dfs(index+1, total - nums[index]) + dfs(index+1, total + nums[index])

            return cache[(index, total)]

        return dfs(0, 0)
        #return ways[0]
