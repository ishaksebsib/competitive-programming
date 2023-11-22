# LINK : https://leetcode.com/problems/string-to-integer-atoi/submissions/1097162602/ 

class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Read and ignore leading whitespace
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        # Step 2: Check for '+' or '-'
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        else:
            sign = 1

        # Step 3: Read characters until non-digit or end of input
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            # Step 4: Check for overflow before updating result
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
                return (2**31 - 1) if sign == 1 else -2**31
            result = result * 10 + digit
            i += 1

        # Step 5: Apply sign and return the result
        return sign * result

