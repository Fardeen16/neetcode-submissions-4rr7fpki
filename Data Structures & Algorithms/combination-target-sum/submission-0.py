class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        TC = O(2^t)
        '''

        ans = []

        curr_window = []

        def backtrack(cur_sum, index):
            if index >= len(nums) or cur_sum > target:
                return
            if cur_sum == target:
                ans.append(curr_window[:])
                return
            
            #choose this number
            curr_window.append(nums[index])
            backtrack(cur_sum + nums[index], index)
            curr_window.pop()

            #not choose ths number
            backtrack(cur_sum, index+1)
        
        backtrack(0, 0)
        return ans