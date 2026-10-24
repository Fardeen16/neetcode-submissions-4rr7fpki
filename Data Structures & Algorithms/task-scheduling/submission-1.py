class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_dict = Counter(tasks)
        counts = [-val for val in count_dict.values()]
        heapq.heapify(counts)
        time = 0
        q = deque()

        while counts or q:
            time += 1
            #if item in heap
            if counts:
                val = 1 + heapq.heappop(counts)
                if val:
                    q.append([val, time + n])

            #if item in q
            if q and q[0][1] == time:
                val , t = q.popleft()
                heapq.heappush(counts, val)
        return time
                


        