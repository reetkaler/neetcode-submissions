class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first check if length of the strings is the same
        # because if the length isnt the same, its not possible
        # for two strings to be anagrams,
        # so thats a simple case we can check
        if (len(s) != len(t)):
            return False
        
        # now that thats out of the way, we can
        # create two "frequency maps" for the strings
        # using a hashmap we can
        '''
        map each character to its frequency,
        and then we can check if these two
        hashmaps are "equal" by comparing each
        entry.
        now you could probably solve this with
        nested for loops, but that would be a higher
        time complexity.
        using hashmaps we should be able to solve this
        in O(n) time
        
        idk what the space compelxity would be
        '''

        countS, countT = {}, {}

        for c in s:
            if(c in countS):
                countS[c] += 1
            else:
                countS[c] = 1
        
        for c in t:
            if(c in countT):
                countT[c] += 1
            else:
                countT[c] = 1

        for c in s:
            if(c not in countT or countS[c] != countT[c]):
                return False
        
        return True


             
        