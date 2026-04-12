class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #temp = set(s)
        
        t = sorted(t)
        s = sorted(s)

        if len(s) == len(t) and s==t:
            return True
        else:
            return False


    
        