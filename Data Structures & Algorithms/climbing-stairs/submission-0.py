class Solution:
    def climbStairs(self, n: int) -> int:
        # starting at step 1, 1 way to get to 1, 0 to get to 0
        # num of ways to get to a step = num of ways to get to n - 1 + n - 2
        cache = [-1] * n

        def dfs(i):
            if i >= n:
                return i == n #if i = n then valid way to climb but if we overshot then not valid
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        return dfs(0)
            

        