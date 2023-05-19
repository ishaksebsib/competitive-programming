# LINK : https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs):

        dic = {}
        for i in strs:
            temp = "".join(sorted(i))
            
            if dic.get(temp,False):
                dic[temp].append(i)
            else:
                dic[temp] = [i]

        return dic.values()



