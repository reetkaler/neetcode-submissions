class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # list of strings
        # loop through the characters of the
        # first string and check if the chars
        # are matching the chars for the rest
        # of the strings in the list
        # for each character that all the
        # strings have the same, add that
        # character to the answer string
        # time complexity might not be the best

        ans = ""
        count = 0

        for c in strs[0]:
            for s in strs:
                if count >= len(s) or c != s[count]:
                    return ans
            ans += c
            count += 1
            if(count == len(strs[0])):
                return ans
        
        return ans