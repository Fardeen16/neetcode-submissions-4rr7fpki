class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x: x[0])

        for i in range(len(intervals)):
            if res and res[-1][1] >= intervals[i][0]:
                res[-1][1] =  max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res
        