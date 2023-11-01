# LINK : https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydic = {}
        for i,val in enumerate(nums):
            t = target - val
            if t in mydic: 
                return [mydic[t],i]
            mydic[val] = i
        return []
