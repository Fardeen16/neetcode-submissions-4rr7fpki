"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
'''
0, 5, 15
10,20,40

'''
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort to get the start times in increasing order 
        starts = sorted(intervals, key = lambda x: x.start)
        ends = sorted(intervals, key = lambda x: x.end)

        print(starts)

        #make 2 arrays to keep track of start and end times
        start_times = [time.start for time in starts]
        end_times = [time.end for time in ends]
        

        rooms = 0
        max_rooms = 0

        start_room_pointer, end_room_pointer = 0, 0

        while start_room_pointer < len(intervals) :
            # start new meeting if old meeting is greater than new meeting
            if start_times[start_room_pointer] < end_times[end_room_pointer]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                start_room_pointer += 1
            else:
                rooms -= 1
                end_room_pointer += 1

        
        return max_rooms

