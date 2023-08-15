# LINK : https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1
    
        frequency = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
        result = list(frequency.keys())[:k]
        
        return result
        