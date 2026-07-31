class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        curr_window = []

        def backtrack(index):
            if index == len(nums):
                ans.append(curr_window[:])
                return
            #we skip the number
            backtrack(index+1)

            # we include that number
            curr_window.append(nums[index])
            backtrack(index+1)
            curr_window.pop()
            
        
        backtrack(0)
        return ans