class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # new interval comes before curr interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # curr interval comes before newInterval
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            
            # overlap
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        # when we don't find an interval that comes after newInterval
        res.append(newInterval)
        return res