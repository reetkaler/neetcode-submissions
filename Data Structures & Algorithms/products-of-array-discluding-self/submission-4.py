class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # have a prefix and postfix array
        # for output, multiply index before and index after current number from their prefix/postfix arrays
        # repeated work

        # populate prefix array, dont count current element
        output = [1] * len(nums)

        for i in range(1, len(nums)):
            output[i] *= nums[i - 1] * output[i - 1]

        # have to keep postfix separate bc output now holds prefix
        # values and we dont want to multiply twice on accident
        postfix = 1
        for i in range(len(output) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output
        
        # time complexity would be O(n)
        # space complexity would be O(3 * n)
