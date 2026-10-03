class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap
        # find the difference between target and current number
        # mapping numbers to the indices

        map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i
        
        