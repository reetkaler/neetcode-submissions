class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams if have the same characters same amt of times
        # order of characters doesnt matter
        # check if lengths are the same
        if len(s) != len(t):
            return False

        sMap, tMap = {}, {} # map chars to frequencies
        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1

        return sMap == tMap


             
        