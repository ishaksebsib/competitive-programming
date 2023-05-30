class Solution:
  def PredictTheWinner(self, nums: List[int]) -> bool:
      size = len(nums)
      dp = [[0]*(size+1) for _ in range(size+1)]

      dp[0][0] = nums[0]

      for i in range(size-1,-1,-1):
          for j in range(i,size):
              dp[i][j] = max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])

      return True if dp[0][size-1] >= 0 else False
