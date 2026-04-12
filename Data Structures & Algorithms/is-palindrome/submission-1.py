import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.replace(" ", "")
        #s = s.replace("?", "")
        print(s)

        for i in range(int(len(s)/2)):
            if s[i] != s[-(i+1)]:
                print(s[i]+"..." +s[-i])
                return False
            else:
                print(s[i]+"////" +s[-(i+1)])

        return True
                
        