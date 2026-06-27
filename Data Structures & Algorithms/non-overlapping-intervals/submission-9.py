class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # return the min numbers of intervals we need to remove to make the rest
        # of the intervals non-overlapping

        # we want the smalles removal

        intervals.sort(key=lambda x:x[0])

        stk = []

        for start, end in intervals:
            # empty
            if not stk: 
                stk.append([start, end])

            # end is smalller than prev one 
            elif end < stk[-1][1]:
                stk.pop()
                stk.append([start, end])
            
            # end is bigger but we do not know if the start: overlaps with list in stk
            elif start == stk[-1][1]:
                stk.append([start, end])
            
            elif start < stk[-1][1]:
                continue
            
            else:
                stk.append([start, end])


        return len(intervals) - len(stk)

