class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # have a prefix and postfix array
        # for output, multiply index before and index after current number from their prefix/postfix arrays
        
        # populating prefix array
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] *= nums[i-1] * prefix[i - 1]
        
        # populate postfix array
        postfix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] *= nums[i + 1] * postfix[i + 1]
        
        output = [1] * len(nums)
        for i in range(len(output)):
            output[i] = prefix[i] * postfix[i]
        
        return output

        
