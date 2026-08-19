"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        if len(intervals) == 1:
            return 1
        
        intervals.sort(key=lambda x: x.start)
        prev_end = intervals[0].end
        num_room = 0

        for i in range(len(intervals)):
            if intervals[i].start >= prev_end:
                prev_end = intervals[i].end
            else:
                # intervals[i].start < prev_end
                num_room += 1
                prev_end = min(prev_end, intervals[i].end)
        
        return num_room

