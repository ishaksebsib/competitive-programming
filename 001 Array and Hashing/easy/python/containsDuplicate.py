# LINK : https://leetcode.com/problems/contains-duplicate/ 

# MY WAY 

from typing import List


class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


# A Better Way 

class Solution2:
    def containsDuplicate(self, nums):
        mySet = set()
        for i in nums:
            if i in mySet:
                return True
            mySet.add(i)
        return False


