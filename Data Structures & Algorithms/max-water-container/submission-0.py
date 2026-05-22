class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            print(l, r)
            distance = r - l
            height = min(heights[l],heights[r])
            area = distance * height
            max_area = max(area, max_area)
            if height == heights[l]: l += 1
            else: r -= 1
        return max_area

        