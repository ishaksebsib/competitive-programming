# LINK : https://leetcode.com/problems/reverse-integer/ 

# my first sluiton
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -int(str(abs(x))[::-1])
        else:
            x = int(str(x)[::-1])
        
        if x.bit_length() >= 32:
            return 0

        return x
