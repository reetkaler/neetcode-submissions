class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first instinct is to use a priority heap, but this may not be the most optimal solution because popping from a heap is logn which we would have to do k times to get the top k most frequent elements
        # also heapify is O(n)

        # we can use bucket sort to get an O(n) solution
        # where the indexes of our buckets array are the frequencies, and we have a list of values at each index which have that frequency
        # 3 2 2 4 5 
        # 0 1 2 3 4 5
        # [], [3, 4, 5], [2], [], [], []

        # can i assume k is always between 1 and the num of unique elements?
        # what if multiple elements share a frequency at the cutoff?

        # make a frequency hashmap
        freq = {}

        # make our list of lists for bucket sort
        buckets = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for n, c in freq.items():
            buckets[c].append(n)

        res = []
        
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res





        