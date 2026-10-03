class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find the biggest diff between two num
        maxProf = 0
        l, r = 0, 1

        # sliding window -> start with small and expand
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProf = max(maxProf, profit)
            else:
                l = r
            r += 1
        return maxProf