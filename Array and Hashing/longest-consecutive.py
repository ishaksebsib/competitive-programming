class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        lgs = 0

        for num in nums:
            if num - 1 not in num_set:
                curent = num
                curentPointer = 1

                while curent + 1 in num_set:
                    curent += 1
                    curentPointer += 1

                lgs = max(lgs, curentPointer)

        return lgs




