# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mydic = {")":"(","}":"{","]":"["}

        for i in s:
            if stack and i in mydic:
                if stack[-1] == mydic[i]:
                    stack.pop()
                    continue
                return False
            stack.append(i)

        return not stack
