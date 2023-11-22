# LINK : 

# MY WAY 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


# A Better Way 

class Solution:
    def containsDuplicate(self, nums):
        mySet = set()
        for i in nums:
            if i in mySet:
                return True
            mySet.add(i)
        return False


