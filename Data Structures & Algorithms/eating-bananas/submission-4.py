class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h is >= len of piles -> max speed is len of piles x len of piles - 1
        # takes ceil(x / k) time to finish (x is a given pile)
        # we need to find min value of k while making sure koko can eat all piles within the given h hours 
        # upper bound for k is max size of the piles bc if koko can eat the largest pile in one hour, then she can eat any other pile in one hour too

        # m - largest pile
        # n - number of piles

        k = max(piles)
        n = len(piles)
        l, r = 1, max(piles)

        # use binary search to check if values between 1 and k are possible
        while l <= r:
            m = (l + r) // 2
            hoursNeeded = 0
            for pile in piles:
                hoursNeeded += math.ceil(pile/m)
            if hoursNeeded > h:
                l = m + 1
            else:
                k = min(k, m)
                r = m - 1

        return k



        