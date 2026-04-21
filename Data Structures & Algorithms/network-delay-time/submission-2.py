class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        So im given a network, can be connected or not connected
        paths are directed, it can have cycles and multiple paths

        -> Can start a BFS from start node, return once all the nodes are visted
        TC = O(E LogV) SC = O(E)

        '''
        # make adj list
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        min_heap = [(0, k)]
        visit = set()
        max_time = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visit:
                continue
            visit.add(node)
            max_time = max(time, max_time)

            for nei, t in edges[node]:
                if nei not in visit:
                    heapq.heappush(min_heap, (t + time, nei))

        return max_time if n == len(visit) else -1    




