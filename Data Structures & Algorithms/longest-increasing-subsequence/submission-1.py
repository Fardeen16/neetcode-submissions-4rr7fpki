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

        '''
        O(nlogn) soln.

        So at each step, we binar search and replace the right most number        

        '''
        ans = [nums[0]]

        def binary_search(num):
            l, r = 0, len(ans)-1
            while l < r:
                mid = (l+r)//2
                if ans[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            return l

        # ietrate for all ns
        for n in nums[1:]:

        # if less, then bnray search to insert
            if n < ans[-1]:
                index = binary_search(num)
                ans[index] = n
            # else just append
            else:
                ans.append(n)
        # return max len formed so far 
        return len(ans)
