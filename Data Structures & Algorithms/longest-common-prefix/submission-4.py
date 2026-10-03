class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # could do more of a sliding window and use sorted()?
        # because the runtime isnt very good with the for loops
        # could probably use hashmaps or hashset somehow?

        ans = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return ans
            ans += s[i]

        return strs[0]

