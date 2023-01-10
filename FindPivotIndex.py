class Solution:
  def pivotIndex(self, nums: List[int]) -> int:

      tot = sum(nums)
      left = 0

      for index, ele in enumerate(nums):
          right = tot - left - ele
          if right == left:
              return index
          left += ele
      return -1
