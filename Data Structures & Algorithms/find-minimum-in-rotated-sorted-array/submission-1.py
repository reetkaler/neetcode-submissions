class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # edge case: already in sorted order
            if(nums[l] < nums[r]):
                res = min(res, nums[l])
                break
            m = (r + l) // 2
            res = min(res, nums[m])

            # if we're in left portion, search right
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            
        return res





        