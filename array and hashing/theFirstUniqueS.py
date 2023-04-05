# LEETCODE LINK : https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        data = {}
        for i,d in enumerate(s):
            if d in data.keys():
                data[d] = -1
            else:
                data[d] = i

        for i in data.values():
            if i >= 0:
                return i
        return -1