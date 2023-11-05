class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)
        res = []

        for i in n1:
            if i in n2:
                res.append(i)
        
        return res

# old soulution 

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)
        
        return res
