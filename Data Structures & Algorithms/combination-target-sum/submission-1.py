class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(index, arr, total):
            if total == target:
                ans.append(arr[:])
                return
            if total > target or index == n:
                return
            
            arr.append(nums[index])
            backtrack(index, arr, total + nums[index])
            arr.pop()

            backtrack(index+1, arr, total)

        backtrack(0, [], 0)
        return ans





        