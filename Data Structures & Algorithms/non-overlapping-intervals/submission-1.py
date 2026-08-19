class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # return the min numbers of intervals we need to remove to make the rest
        # of the intervals non-overlapping

        # we want the smalles removal

        intervals.sort(key=lambda x:x[0])

        stk = []

        for start, end in intervals:
            if not stk: 
                stk.append([start, end])

            elif end <= stk[-1][1]:
                stk.pop()
                stk.append([start, end])
            
            else:
                stk.append([start, end])
        
        return len(intervals) - len(stk)
