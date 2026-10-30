class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []

        counts = Counter(s)
        min_heap = [[-v, k] for k,v in counts.items()]
        heapq.heapify(min_heap)

        q = deque()

        while min_heap or q:
            if q and not min_heap:
                return ""
            
            count, char = heapq.heappop(min_heap)
            count += 1
            res.append(char)
            
            if q:
                cnt, ch = q.popleft()
                heapq.heappush(min_heap, [cnt, ch])
            
            if count:
                q.append([count, char])

        return "".join(res)
        