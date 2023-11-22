# LINK : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1

        while l < r:
            res = numbers[l] + numbers[r]

            if res < target:
                l+=1
            elif res > target:
                r-=1
            else:
                return [l+1,r+1]
