class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #...[i, temp]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                s_i, s_t = stack.pop()
                res[s_i] = i - s_i
            stack.append([i, t])
        return res
        