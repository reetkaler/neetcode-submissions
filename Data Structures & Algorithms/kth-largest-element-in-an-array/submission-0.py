import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # make a heap
        # do i implement the heap with deque?
        # python's default heap is a min heap
        # iterate through each num in nums and push it to the heap
        # whenever size of the heap > k, pop smallest element
        # this leaves the k-th largest element at k because

        heap = []
        # 4 5 
        for n in nums:
            heapq.heappush(heap, n)
            if k < len(heap):
                heapq.heappop(heap)
            
        return heap[0]

        