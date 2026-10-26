class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        l, r = 0, 0
        res = []

        while r < len(nums):
            while stack and nums[stack[-1]] < nums[r]:
                stack.pop()
            stack.append(r)
            
            if stack[0] < l:
                stack.popleft()
            
            if (r-l+1) >= k:
                res.append(nums[stack[0]])
                l += 1
            r += 1
        return res
        