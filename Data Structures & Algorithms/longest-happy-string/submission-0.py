class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        given_dict = {"a": a, "b": b, "c": c}

        min_heap = [[-v, k] for k, v in given_dict.items() if v != 0]
        res = []
        print(min_heap)
        heapq.heapify(min_heap)
        while min_heap:
            count, char = heapq.heappop(min_heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                #skip this
                if not min_heap:
                    break
                count2, char2 = heapq.heappop(min_heap)
                res.append(char2)
                count2 += 1
                if count2:
                    heapq.heappush(min_heap, [count2, char2])
            else:
                res.append(char)
                count += 1
            if count:
                heapq.heappush(min_heap, [count, char])


        return "".join(res)
        #print(min_heap)
