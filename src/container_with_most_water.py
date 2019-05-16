class Solution:

    def container_with_most_water(self, heights):
        left = 0
        right = len(heights) - 1
        current_level = self.calc_height_between(heights, left, right)
        while left < right - 1:
            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            current_level = max(current_level, self.calc_height_between(heights, left, right))
        return current_level

    def calc_height_between(self, heights, i, j):
        return min(heights[i], heights[j]) * abs(j - i)

