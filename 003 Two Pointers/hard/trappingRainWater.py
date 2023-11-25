# LINK : https://leetcode.com/problems/trapping-rain-water/description/

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        lm = height[l]
        rm = height[r]

        while l < r:
            lm = max(lm, height[l])
            rm = max(rm, height[r])

            if lm < rm:
                res += lm - height[l]
                l += 1
            else:
                res += rm - height[r]
                r -= 1

        return res
