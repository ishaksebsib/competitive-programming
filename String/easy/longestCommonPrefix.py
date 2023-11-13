# LINK : https://leetcode.com/problems/longest-common-prefix/description/

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

