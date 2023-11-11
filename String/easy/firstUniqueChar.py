# LINK : https://leetcode.com/problems/first-unique-character-in-a-string/description/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydic = {}
        for i in s:
            mydic[i] = mydic.get(i,0) + 1
        
        for i,val in enumerate(s):
            if mydic[val] == 1:
                return i

        return -1
