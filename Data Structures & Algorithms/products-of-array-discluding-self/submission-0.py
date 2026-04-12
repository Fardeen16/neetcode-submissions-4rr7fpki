class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            ans = 1
            j = 0
            while j<len(nums):
                if i!=j:
                    ans = ans * nums[j]
                    j+=1
                else:
                    j+=1
                
            
            res.append(ans)

        return res        