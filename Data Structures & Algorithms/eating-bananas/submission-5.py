class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # upper bound of k is max in piles
        k = max(piles)

        # can get the num of hours it takes to finish a pile with ceil(pile/k) at a rate of k bananas per hour
        l, r = 1, k

        # use binary search between values 1 and largest pile
        # to find min value for k

        # at each middle value, check if this k works by looping through
        # piles and calculating how many hours it would take to finish all the bananas
        # if hoursneeded < h then set our new k to mid and keep searching
        # through left portion
        # if hoursneeded > h then search through right portion 
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours <= h:
                k = min(mid, k)
                r = mid - 1
            else:
                l = mid + 1
        return k
        # space is O(1), time complexity is O(n * logm)



        