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
        minK = float('inf')
        piles.sort()
        totalHours = 0

        l = 0
        r = len(piles)

        while l < r:
            mid = l + ((r-l) // 2)
            print(f"mid: {mid}")
            print(f"piles[mid]: {piles[mid]}")

            for pile in piles:
                hour = pile / piles[mid]
                totalHours += math.ceil(hour)

            print(f"totalH: {totalHours}")

            if totalHours <= h:
                minK = min(minK, piles[mid])
                print(minK)
                r = mid
                totalHours = 0

            elif totalHours > h:
                print("1")
                l = mid + 1
                totalHours = 0
        
        
        return minK


        

        
