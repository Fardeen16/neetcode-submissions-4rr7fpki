class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        So im given a network, can be connected or not connected
        paths are directed, it can have cycles and multiple paths

        -> Can start a BFS from start node, return once all the nodes are visted
        TC = O(E LogV) SC = O(E)

        '''

        # start by making an adj list
        adj_list = defaultdict(list)
        for source, destination, weight in times:
            adj_list[source].append((weight, destination))

        # initialaize all varaibles
        min_heap = [[0, k]]
        visited_set = set()
        total_time = 0

        # start BFS
        while min_heap:
            total_distance, node = heapq.heappop(min_heap)

            if node in visited_set:
                continue
            
            visited_set.add(node)
            total_time = max(total_time, total_distance)

            for nei_wt, nei in adj_list[node]:
                heapq.heappush(min_heap, (total_distance + nei_wt, nei))
        
        return total_time if len(visited_set) == n else -1


        