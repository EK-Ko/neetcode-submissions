import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #if k = 1, hours-required = sum(piles)
        #if k = maxVal(piles), hours-required = len(piles)
        # k's range is 1-maxVal(piles)

        #gotta check if hours spent is <= h
        #if it is, return that value k
        #if not, try other

        #First find the maximum value in piles
        max_pile = max(piles)

        L, R = 1, max_pile
        res = max(piles)

        while L <= R:
            mid = L + (R-L) // 2
            hoursSpent = self.totalHoursSpent(piles, mid)
            if hoursSpent <= h:
                res = mid
                R = mid - 1
            else:
                L = mid + 1
            
        return res


    def totalHoursSpent(self, piles: List[int], n: int) -> int:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/n)
        return hours
