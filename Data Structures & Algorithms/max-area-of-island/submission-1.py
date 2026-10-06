class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        visited = set()

        # O (n * m) visiting every element in the grid
        # space complexity - call stack of dfs

        def dfs(r, c) -> int:
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return 0
            if grid[r][c] == 0:
                return 0
            if grid[r][c] == 1:
                if (r, c) in visited:
                    return 0
                else:
                    visited.add((r, c))
                    return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        # nested for loop each index in grid
        # whenever we reach a 1 and its not visited yet, we run dfs
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if (r, c) not in visited and grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        return area


            

            