import heapq


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        h = {}
        # tracking count of tasks
        for i in tasks:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1

        heap = [-i for i in h.values()]
        # heapifying the heap
        heapq.heapify(heap)
        # initialise the queue
        q = []
        time = 0  # our ans

        while heap or q:
            time += 1  # increment count by one unit
            # if heap is not empty
            if heap:
                """
                incrementing by one as we assign negative value to build max heap
                """
                curr_cnt = heapq.heappop(heap) + 1
                # appending the current task in queue as it is remaining
                if curr_cnt:
                    q.append(
                        (time + n + 1, curr_cnt)
                    )  # time+n+1 is because tiem+n+1 is the time when the curr task executes again
            # if queue is not empty and also first task of queue executes at time time+1
            if q and q[0][0] == time + 1:
                heapq.heappush(heap, q.pop(0)[1])

        # returning answer
        return time


# we are creating a max heap of count of the values
# we will keep track f time
# when we process a task just increment the time
# then pop max value from queue decrement it by one and add it to queue along with when that letter can be used next time so time + n
# check if any queuq value are avaliable then add it to our max heap
# and repeat the same process
