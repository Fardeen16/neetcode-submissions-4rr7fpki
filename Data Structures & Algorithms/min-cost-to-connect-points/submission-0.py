class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        Prim's algo, will check edge form point a to all other points, and choose the min distance
        at each heap pop.

        TC = O(V^2)

        '''
        # adjecency list to store all the point name to coords
        #adj_list = [index : point for index, point in enumerate(points)]
 
        # declare all viarables
        min_heap = [[0, 0]] #[distance, point]
        total_distance = 0
        visited_set = set()
        n = len(points)

        # pop min heap while all nodes are visited
        while min_heap:
            dist, coord = heapq.heappop(min_heap)

            if coord in visited_set:
                continue
            #update distance each at each pop
            total_distance += dist
            visited_set.add(coord)

            x1, y1 = points[coord]
            #find and add all the neighbours in the heap and later pop accordingly
            for j in range(n):
                if j not in visited_set:
                    x2, y2 = points[j]
                    point_dist = abs(x2 - x1) + abs(y2 - y1)
                    heapq.heappush(min_heap, (point_dist, j))
        return total_distance


        