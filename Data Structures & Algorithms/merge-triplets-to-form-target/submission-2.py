class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = [0, 0, 0]

        for i in range(len(triplets)):
            x1, y1, z1 = triplets[i]
            if x1 > target[0] or y1 > target[1] or z1 > target[2]:
                    continue
            ans[0] = max(ans[0], x1)
            ans[1] = max(ans[1], y1)
            ans[2] = max(ans[2], z1)
            if ans == target:
                return True
            print(ans)
        return False
        