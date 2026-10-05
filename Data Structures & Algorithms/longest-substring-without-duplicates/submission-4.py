class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a hashset and two pointers
        if not s:
            return 0
        if len(s) == 1:
            return 1

        l, r = 0, 1
        seen = set()
        seen.add(s[l])
        longest = 1
        currLen = 1

        # as we grow the window, check if that character is in our hash set
        # if we did, pop from the left until its not there anymore
        # decrement our current length
        # keep track of our largest substring

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                if l < r:
                    l += 1
                    currLen -= 1
            seen.add(s[r])
            currLen += 1
            r += 1
            longest = max(longest, currLen)
        return longest

        