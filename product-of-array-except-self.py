class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        theLength=len(nums)
        res=[1]*theLength
        first = 1
        last = 1
        for i in range(theLength):
            res[i] *= first
            first = first*nums[i]
            res[theLength-i-1] *= last
            last = last*nums[theLength-i-1]
        return(res)
