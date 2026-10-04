class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ops = target[0]
        # only need to increment ops when number is greater than the number before it
        for i in range(1, len(target)):
            if target[i - 1] < target[i]:
                ops += (target[i] - target[i - 1])
        
        return ops
