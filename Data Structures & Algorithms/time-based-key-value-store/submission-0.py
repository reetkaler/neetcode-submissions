class TimeMap:
    # map keys to values and timestamps
    # im thinking we can use a hash map to do this
    # accessing from a hash map is O(1)
    # inserting into a hash map is O(1) i think though

    def __init__(self):
        self.store = {}
        
    # all timestamps of set are increasing
    def set(self, key: str, value: str, timestamp: int) -> None:
        # map each key to a list of pairs, (timestamp, value)
        # this will naturally stay sorted
        pair = [timestamp, value]
        if key not in self.store:
            self.store[key] = []
        self.store[key].append(pair)

    def get(self, key: str, timestamp: int) -> str:
        # returns value with the largest timestamp_prev, if none, return ""
        # use binary search and for each middle, check if that timestamp
        # exists in our data structure, if it does, binary search
        # to the right half,
        # if it doesnt, binary search from the left half

        # timestamps are in sorted order
        if key not in self.store:
            return ""
        
        res = ""
        
        # use binary search and loop through timestamp pairs in store
        l, r = 0, len(self.store[key]) - 1

        while l <= r:
            mid = (l + r) // 2
            if self.store[key][mid][0] <= timestamp:
                # check right half
                res = self.store[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res