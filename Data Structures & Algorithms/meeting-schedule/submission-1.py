"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)

        for j in range(1, len(intervals)):
            prev = intervals[j-1]
            curr = intervals[j]

            if curr.start < prev.end:
                return False

        return True 

