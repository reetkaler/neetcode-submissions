class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        # water at a given index = min(maxleft, maxright) - height
        # if negative, round up to 0
        # answer is the sum of all units of water

        # two pointers
        # if leftmax < rightmax, we can calculate the amount of water at the leftmax position and then move left pointer
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
        
