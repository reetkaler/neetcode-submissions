class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group all anagrams together into sublists
        # order doesnt matter
        # create freq hashmaps for each string
        # check if current string has the same frequency map as another
        # if they do, group those strings together
        # return all appended strings

        # can map array of character counts to list of
        # strings that have that character count

        map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            map[tuple(count)].append(s)
        return list(map.values())

        # time complexity would be O(n * k) where n is the number of strings and k is the max string length
                
        