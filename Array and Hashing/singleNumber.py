# LINK : https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            # print(f'num = {num} , result = {res} ^ {num} = {res^num}')
            res ^= num # XOR operation
        return res