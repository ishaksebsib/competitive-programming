# Link : "https://leetcode.com/problems/intersection-of-two-arrays-ii/"


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dic = {}

        for i in nums1:
            dic[i] = dic.get(i,0) + 1
        
        for i in nums2:
            if i in dic and dic[i] > 0:
                res.append(i)
                dic[i] -= 1

        return res