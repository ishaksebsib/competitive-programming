# LEET CODE LINK : https://leetcode.com/problems/contains-duplicate/description/


class Solution:
    def containsDuplicate(self, nums):
        mySet = set()
        for i in nums:
            if i in mySet:
                return True
            mySet.add(i)
        return False

