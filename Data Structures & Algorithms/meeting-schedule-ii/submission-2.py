import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        rooms = []  # min-heap of meeting end times

        for interval in intervals:
            # If the earliest-ending room is free, reuse it
            if rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)

            # Put current meeting into a room
            heapq.heappush(rooms, interval.end)

        return len(rooms)