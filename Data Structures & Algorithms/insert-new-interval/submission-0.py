class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # if newInterval comes before current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # if newIntervals comes after the cuurent interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # we keep updating the NewInterval to adjust overlapping
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        res.append(newInterval)
        return res
            