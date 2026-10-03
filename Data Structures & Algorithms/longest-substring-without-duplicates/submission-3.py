class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 1
        curr = 1
        # declare left and right pointers
        l, r = 0, 1
        # use a hash set to check if character is present in window
        seq = set()
        seq.add(s[l])
        # make window wider by increasing r
        while r < len(s):
            # if encounter a duplicate, increment l until no more dupe
            if s[r] in seq:
                # remove from hashset as u shrink the window
                while s[r] in seq:
                    seq.remove(s[l])
                    l += 1
                    curr -= 1
            seq.add(s[r])
            r += 1
            curr += 1
            # at each iteration u update result with length of current window
            res = max(curr, res)
        return res

        
        


        