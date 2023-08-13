# Link : https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums):
        return sum(range(len(nums) +1)) - sum(nums)
