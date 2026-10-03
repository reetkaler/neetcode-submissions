class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # could do a nested for loop -> O(n^2) time complexity
        # could use a hashset
        # could sort the array
        # convert list to a hashset and see if the lengths are the same
        # return TRUE if theres a duplicate
        # False if no duplicates

        s = set()

        for n in nums:
            if n in s:
                return True
            s.add(n)
        
        return False


        