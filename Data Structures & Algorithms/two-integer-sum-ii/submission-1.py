class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        l, r = 0, len(numbers)-1
        res = []

        while l < r:
            print(numbers[l])
            print(numbers[r])
            if (numbers[l] + numbers[r]) > target:
                r -= 1
            elif (numbers[l] + numbers[r]) < target:
                l += 1
            else:
                res.append(l+1)
                res.append(r+1)
                return res

        