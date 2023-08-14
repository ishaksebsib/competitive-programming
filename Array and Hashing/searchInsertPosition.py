# LINK : https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums,target):
        for i,val in enumerate(nums):
            if val >= target:
                return i
        return len(nums)
