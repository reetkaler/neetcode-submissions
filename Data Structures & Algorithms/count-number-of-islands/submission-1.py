from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # continuous island until surrounded by 0's/bounds
        count = 0
        visited = set()

        # depth first search
        # have a seen queue to make sure we dont double count 1's

        # for dfs go right left up or down
        # check if we're out of bounds
        # check if we're at a 0
        # if we're at a 1, add to seen queue (use indices?)

        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return None
            if grid[r][c] == "0":
                return None
            if grid[r][c] == "1":
                if (r, c) in visited:
                    return None
                else:
                    visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r,c-1)

        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    count += 1
        return count

        
