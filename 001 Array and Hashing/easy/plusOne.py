# LINK : https://leetcode.com/problems/plus-one/ 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry,i = 1,len(digits) - 1

        while carry:
            if i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.insert(0,carry)
                carry = 0
            i-=1
            
        return digits
