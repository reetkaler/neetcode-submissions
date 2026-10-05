class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        l, r = 0, len(heights) - 1
        area = 0

        # have left and right pointers
        while l < r:
            currArea = min(heights[l], heights[r]) * (r - l)
            if (heights[l] > heights[r]):
                r -= 1
            else:
                l += 1
            area = max(area, currArea)

        return area

        # [1, 0, 0, 2]
        # 0. 1. 2.  3 (3 - 1) = 2



        