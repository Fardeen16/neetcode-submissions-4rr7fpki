class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_window = defaultdict(int)
        
        min_len = float("inf")
        c_l, c_r = 0, 0

        if len(t) > len(s):
            return ""

        for char in t:
            target_window[char] += 1
        
        l, r = 0, 0
        formed, total = 0, len(target_window)
        while r < len(s):
            if s[r] in target_window:
                target_window[s[r]] -= 1
                if target_window[s[r]] == 0:
                    formed += 1
            while l <= r and formed == total:
                curr_len = r - l + 1
                if curr_len < min_len:
                    min_len = curr_len
                    c_l, c_r = l, r+1
                char = s[l]
                if char in target_window:
                    if target_window[char] == 0:
                        formed -= 1
                    target_window[char] += 1
                l += 1
            r += 1
        return "" if min_len == float("inf") else s[c_l: c_r]
        

        