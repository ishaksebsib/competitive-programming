class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}
        count2 = {}
        res = []

        for i in nums1:
            count1[i] = count1.get(i,0) + 1
        
        for i in nums2:
            count2[i] = count2.get(i,0) + 1

        for i in count1:
            if i in count2:
                res.extend([i] * min(count1[i],count2[i]))
        
        return res
