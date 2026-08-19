"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # true if all meetings can be filled w/o conflict
        intervals.sort(key=lambda x: x.start)
        prev_end = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start >= prev_end:
                prev_end = intervals[i].end

            elif intervals[i].start < prev_end:
                return False
        
        return True

