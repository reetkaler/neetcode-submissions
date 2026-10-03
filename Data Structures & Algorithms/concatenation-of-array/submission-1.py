class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # nums = [1, 4, 1, 2] len = 4 = n
        # ans = [1, 4, x, x, 1, 4, x, x ] len = 2n = 8
        # ans[0] == nums[0]
        # ans[0 + 4] = nums[0]
        # ans[1] = nums[1]
        # ans[1 + 4] = nums[1]
        # nums repeated

        # looping through twice would be O(n^2)
        # O(n)

        n = len(nums)
        ans = [0] * (2*n)
        for i, num in enumerate(nums):
            ans[i] = ans[i+n] = num

        return ans