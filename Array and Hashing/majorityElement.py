# LINK : https://leetcode.com/problems/majority-element/solutions/2379248/very-easy-100-fully-explained-c-java-python-js-c-python3/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = None
        count = 0

        for i in nums:
            if count == 0:
                res = i
            if i == res:
                count +=1
            else:
                count -= 1

        return res