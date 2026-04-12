class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # if len(nums) == 0:
        #     return 0

        # ans = 1 
        # nums.sort()
        # start = nums[0]
        

        # for i in range(len(nums)):
        #     if nums[i] == start + 1:
        #         ans+=1
        #         start = nums[i]
        #     # else:
        #     #     pass
        # return ans
        

        if len(nums) == 0:
            return 0
        ans_set = set(nums)
        longest_len = 1

        for n in ans_set:
            if n-1 not in ans_set:
                curr_n = n
                curr_len = 1

                while curr_n+1 in ans_set:
                    curr_n += 1
                    curr_len += 1
                longest_len = max(longest_len,curr_len)

        return longest_len