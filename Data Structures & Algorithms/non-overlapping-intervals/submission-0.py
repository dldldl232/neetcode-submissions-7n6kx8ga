class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # return the min numbers of intervals we need to remove to make the rest
        # of the intervals non-overlapping

        intervals.sort(key=lambda x:x[0])

        res = []

        for start, end in intervals:
            if not res or start >= res[-1][1]:
                res.append([start, end])
        
        return len(intervals) - len(res)

        