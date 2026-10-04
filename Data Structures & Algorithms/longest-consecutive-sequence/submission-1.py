class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # only need to consider a number to be the beginning of a sequence if
        # num - 1 is not in the sequence
        # use a hash set to access with O(1)
        
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while(num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


        