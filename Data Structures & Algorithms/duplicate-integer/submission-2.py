class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a hash set to track seen values
        # as we populate the set, check if that val is already in the set, if true, then return true
        # if we get through the map 

        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False


        