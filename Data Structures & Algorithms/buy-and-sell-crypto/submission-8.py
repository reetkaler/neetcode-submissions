class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return max profit
        # profit[future] - profit[present]
        # find greatest diff between values (bigger val is later)
        # num of days doesnt have an impact on the profit 1 2 3 4    1 1 1 4

        # two pointers
        # left - smallest value
        # right - biggest value
        # 0 len(prices) - 1
        l, r = 0, 1

        if not prices or len(prices) == 1:
            return 0

        # min l and min r 
        maxProfit = prices[r] - prices[l]

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1
        return maxProfit if maxProfit > 0 else 0


        