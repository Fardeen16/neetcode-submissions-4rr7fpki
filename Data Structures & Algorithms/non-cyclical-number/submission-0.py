class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def calculate(n):
            ans = 0
            while n > 0:
                digit = n % 10
                ans += (digit * digit)
                n //= 10
            return ans

        while n != 1:
            num = calculate(n)
            if num in seen:
                return False
            seen.add(num)
            n = num 
        
        return True