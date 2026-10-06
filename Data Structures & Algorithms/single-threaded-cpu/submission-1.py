class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # [enqueuetime, dequeuetime]
        # one task at a time

        # if idle and no tasks, stay idle
        # if idle and tasks, choose shortest processing time (if tie, choose smaller index)
        # once start to process, cpu will process the entire task without stopping

        # use a min heap where the key is the processing time
        # so we can easily pop the first one
        # return order (keep track of indices)

        # sort tasks by their enqueue time
        # before putting into the heap, preserve og indices before sorting by enqueue time

        # keep track of the time so you dont jump to
        # tasks that arent done being queued yet
        # add tasks to the heap when enqueueTime <= time
        # add processing time of a task to time
        # if cpu is free, jump time to next available task
        heap = []
        res = []
        
        # preserve original indices
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key=lambda t: t[0]) # sort by enqueue time 
        # tc - O(nlogn)
        i, time = 0, tasks[0][0]

        # sorted by enqueueTime
        while heap or i < len(tasks): # heap operations are (Ologn) then O(n) for iterating through values
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]]) # push processing time and original index
                i += 1
            if not heap:
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(heap)
                time += procTime
                res.append(index)
        return res