# LINK : https://leetcode.com/problems/longest-common-prefix/description/

# more efficent soution 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        l = strs[0]
        r = strs[-1]
        res = ""

        for i in range(len(l)):
            if l[i] == r[i]:
                res+=l[i]
                continue
            return res

        return res

# my old solution 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        expre = strs[0]

        for i in range(1,len(strs)):
            k = 0
            while k <= len(expre):
                if strs[i][:k] == expre[:k]:
                    k+=1
                else:
                    break
            expre = expre[:k-1]
        return expre

