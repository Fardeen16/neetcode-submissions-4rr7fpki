class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        need to find the no. of ways i can make the sequence

        when i can make a seq.
        ->end of t, it means the sequence is valid

        if char in s does not match in t, move index in s;
        is s reaches end, no valid sequence found

        Also, at any martching index, i have 2 choices:
        -> choose that index
        -> choose the next index

        '''

        cache = {} # (i, j): num of ways

        # i: index of s, j index of t 
        def backtrack(i, j):
            # base conditions
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            result = 0
            # choices i make    
            if s[i] == t[j]:
                # either move index t consider next one
                result += backtrack(i+1, j)
                #either consider it
                result += backtrack(i+1, j+1)
            else:
                result += backtrack(i+1, j)
            cache[(i, j)] = result
            return cache[(i, j)]

        return backtrack(0, 0)






