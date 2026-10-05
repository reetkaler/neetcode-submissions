class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check if array is already sorted
        # one half is guaranteed to be sorted bc only one half can have the "drop" in it
        # check which half is sorted
        # then check if target falls within the sorted half -> if yes, run binary search on sorted half
        # if no, go to other half and run again
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            # base case (found target)
            if (nums[m] == target):
                return m
            # left half is sorted
            if (nums[l] <= nums[m]):
                if (nums[l] <= target <= nums[m]):
                    # target is in left half
                    r = m - 1
                else:
                    # target is in right half
                    l = m + 1
            # right half is sorted
            else:
                if (nums[m] <= target <= nums[r]):
                    l = m + 1
                else:
                    r = m - 1
        return -1
            


        
        