"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#0______________________________40
#    5_____10
#                15_____20

# [0, 5, 15]
# [10, 20, 40]

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        meet_count = 0
        max_meet = 0
        s = 0
        e = 0

        while s < len(intervals):
            if start[s] < end[e]:
                meet_count += 1
                s += 1
            else:
                meet_count -= 1
                e += 1
            max_meet = max(max_meet, meet_count)

        return max_meet




        