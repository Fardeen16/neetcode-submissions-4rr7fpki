class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        n_s = 0
        while n_s != slow:
            n_s = nums[n_s]
            slow = nums[slow]
        
        return slow
        

        

        