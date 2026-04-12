"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals.sort(key = lambda i: i.start)

        # days = [[intervals[0].start, intervals[0].end]]#days = {[], [], []...}

        # for i in range(1, len(intervals)):
        #     curr_s, curr_end = intervals[i].start, intervals[i].end
        #     print("in i ")
        #     day_len= len(days)
        #     for j in range(day_len):
        #         print(days)
        #         if curr_s >= days[j][-1]:
        #             days[j].append([curr_s, curr_end])
        #             print("in if")
                    
        #         else:
        #             days.append([curr_s, curr_end])
        #             print("in else")
                    

        # return len(days)
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s = e = 0
        count = res = 0

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)

        return res



#        return days 
        