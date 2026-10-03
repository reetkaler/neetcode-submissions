class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return[map[diff], i]
            map[n] = i
        return

        # nums = [3, 4, 5, 6]
        # target = 7

        # map = {[3, 0], }
        # diff = 3
        # 0, 1