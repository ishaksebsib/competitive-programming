# LINK : https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs):
        dic = {}

        for i in strs:
            temp = ''.join(sorted(i))
            dic[temp] = dic.get(temp,[]) + [i]

        return dic.values()







