# LINK : https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:         
        uni = 0
        for i in nums:
            uni ^= i
        return uni
        