class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        time = 0

        char_count = Counter(tasks)
        max_heap = [-i for i in char_count.values()]
        heapq.heapify(max_heap)


        while max_heap or q:
            time += 1
            # we pop task from heap
            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    q.append([count, time + n])

            # we add task to queue which wasnt done
            if q and q[0][1] == time:
                count, t = q.popleft()
                heapq.heappush(max_heap, count)
        
        return time 
        