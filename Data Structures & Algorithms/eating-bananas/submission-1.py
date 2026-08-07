import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # eat k bananas from that pile
        # if pile has less than k bananas, we can finish eating pile, but cannot eat from
        # another pile in the same hour. 

        """
        for every i sum( math.ceil(piles[i] // eating_rate) ) < h
        return minimum eating_rate (aka k)

        brute force

        """
        
        l, r = 1, max(piles)

        while l < r:
            mid = l + ((r-l) // 2)
            total_hours = sum(math.ceil(pile/mid) for pile in piles)

            if total_hours <= h:
                r = mid # trying to find sthg smaller
            elif total_hours > h:
                l = mid + 1 # does not work
        
        return r


        

        
