class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # if value to the right is less than or equal to value to the left, we need to include it in substring
        # if value to the right is greater than value to the right, we don't include it in substring

        # we can always increment values next to eachother as long as their values dont need to be less than the current value

        # first element only need target[0] # of operations, after target[i] only need additional if target[i] > target[i - 1]
        # num of extra required is target[i] - target[i - 1]
        ops = target[0]
        # increment count of ops if target[i] > target[i - 1]
        for i in range((len(target) - 1)):
            if target[i] < target[i + 1]:
                ops += target[i + 1] - target[i]
        return ops
