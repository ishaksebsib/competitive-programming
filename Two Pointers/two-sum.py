# LINK = https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/953231863/

class Solution:
    def twoSum(self, numbers, target: int):
        l, r = 0, len(numbers) - 1

        while l < r:
            cruntSum = numbers[l] + numbers[r]

            if cruntSum > target:
                r -= 1
            elif cruntSum < target:
                l += 1
            else:
                return [l+1, r+1]
