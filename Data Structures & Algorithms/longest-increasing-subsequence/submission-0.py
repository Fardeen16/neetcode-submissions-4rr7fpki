class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        can be doen in O(nlogn) too
        '''

        # O(n**2) soln:
        LIS = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

        