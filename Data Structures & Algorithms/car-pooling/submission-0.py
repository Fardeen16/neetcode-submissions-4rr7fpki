class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_heap = [] #[end time, num of passenger]
        curr_capacity = 0
        trips.sort(key = lambda x:x[1] )

        for trip in trips:
            passenger, start, end = trip

            while min_heap and start >= min_heap[0][0]:
                end_time, passen = heapq.heappop(min_heap)
                curr_capacity -= passen
            
            curr_capacity += passenger

            if curr_capacity > capacity:
                return False
            
            heapq.heappush(min_heap, [end, passenger])
        
        return True
            
            

