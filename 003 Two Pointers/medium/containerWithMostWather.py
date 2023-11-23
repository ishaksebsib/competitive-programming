# LINK : https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0

        while l < r:
            currentArea = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, currentArea)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea
