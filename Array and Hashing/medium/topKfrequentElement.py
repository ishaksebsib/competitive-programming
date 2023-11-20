# LINK : https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydic = {}
        grab = [[] for i in range(len(nums) + 1)]

        for i in nums:
            mydic[i] = mydic.get(i,0) + 1

        for i,val in mydic.items():
            grab[val].append(i)

        res = []
        for i in range(len(grab) - 1, 0, -1):
            for n in grab[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
