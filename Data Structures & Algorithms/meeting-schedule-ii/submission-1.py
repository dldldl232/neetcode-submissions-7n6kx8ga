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
        num_room = []

        for i in range(len(intervals)):
            # if not num_room:
            #     num_room.append([intervals[i].end])
            
            if len(num_room) == 1:
                if num_room[0][-1] <= intervals[i].start:
                    num_room.append(intervals[i].end)
            
            for j in range(len(num_room)):
                if num_room[j][-1] <= intervals[i].start:
                    num_room[j].append(intervals[i].end)
                
            num_room.append([intervals[i].end])
        
        print(num_room)
        return len(num_room)

