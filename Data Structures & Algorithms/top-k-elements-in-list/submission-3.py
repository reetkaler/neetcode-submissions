class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap implemented with a deque
        # return k most frequent elements within arr
        # order doesnt matter
        # use bucket sort to create n buckets
        # group nums based on their freq from 1 to n
        # pick top k nums from the buckets
        # starting from n down to 1
        
        # get freq of each element
        map = {} # element to freq
        for n in nums:
            map[n] = map.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)] # index stores elements w freq i
        for key, val in map.items():
            buckets[val].append(key)

        res = []
        for i in range((len(buckets) - 1), -1, -1):
            for val in buckets[i]:
                res.append(val)
                if len(res) == k:
                    return res



        