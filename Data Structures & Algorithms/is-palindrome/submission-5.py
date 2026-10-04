class Solution:
    def isPalindrome(self, s: str) -> bool:
        # separate into even and odd
        # dont consider spaces and convert uppercase letters to lower
        l, r = 0, (len(s)-1)

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if (s[l].lower() != s[r].lower()):
                return False
            l += 1
            r -= 1

        return True
        