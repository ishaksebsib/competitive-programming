# LINK : https://leetcode.com/problems/group-anagrams/description/ 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydic = defaultdict(list)

        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord('a')] += 1
                
            mydic[str(count)].append(i)

        return mydic.values()


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
