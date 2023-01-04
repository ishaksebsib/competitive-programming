class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0 
        mydic = {}  
        
        for num in nums:
            if ((k-num) in mydic) and (mydic[k-num] > 0):
                mydic[k-num] -= 1
                count += 1
            elif num not in mydic:
                mydic[num] = 1
            else:
                mydic[num] += 1

        return count
