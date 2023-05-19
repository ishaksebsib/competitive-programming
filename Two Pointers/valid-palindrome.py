# LINK : https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s):
        newlist = ""

        for i in s:
            if i.isalnum():
                newlist += i.lower()

        return newlist == newlist[::-1]
