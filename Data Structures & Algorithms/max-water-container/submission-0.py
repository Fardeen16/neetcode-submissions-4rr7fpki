class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0

        i = 0
        j = len(heights) - 1
        print(j)
        print(heights[j])

        while i<j:
            area = min(heights[i], heights[j]) * (j-i)
            print("area", area)
            max_area = max(area, max_area)
            print("max_area", max_area)

            if heights[j] > heights[i]:
                i += 1
                #h = height[i]
            else:
                j -= 1
                #h = height[j]
        
        return max_area




        