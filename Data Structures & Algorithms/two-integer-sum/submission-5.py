class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # could use a nested for loop to check if each possible pair adds up to target, this would be O(n^2) time complexity though
        # a more optimal solution would be to build a hash map with each number in the array and it's complement
        # when populating the hash map, we can check if the complement is in the map, if not, we just add the current number and then keep traversing
        # this way we only have to visit each value once, making the time complexity linear (O(n)) instead of exponential

        # search through values before current number so we dont overcount (count the current val if we populate the hash map first)
        map = {} # complement to index

        for i, n in enumerate(nums):
            complement = target - n
            if complement in map:
                return [map[complement], i]

            map[n] = i