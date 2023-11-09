# LINK : https://leetcode.com/problems/reverse-integer/ 

# my first sluiton
class Solution:
    def reverse(self, x: int) -> int:
        h = 2**31 - 1
        l = -2**31

        if x < 0:
            x = -int(str(abs(x))[::-1])
        else:
            x = int(str(x)[::-1])
        
        if x > h or x < l:
            return 0

        return x
