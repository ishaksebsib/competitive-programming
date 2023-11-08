# LINK : https://leetcode.com/problems/group-anagrams/description/ 



# my first version 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydic = {}

        for i in strs:
            target = "".join(sorted(i))
            if target in mydic:
                mydic[target].append(i)
                continue
            mydic[target] = [i]

        return mydic.values()       
