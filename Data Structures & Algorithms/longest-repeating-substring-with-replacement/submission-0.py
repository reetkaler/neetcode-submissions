class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find the character to replace with by finding the most frequent char in string

        # num of changes that we're making <= k

        # make my window smaller if not valid

        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

        