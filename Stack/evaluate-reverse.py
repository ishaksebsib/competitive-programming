# PROBLEM LINK : https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(int(i))
            else:
                b, a = stack.pop(), stack.pop()
                if i == "+": 
                    stack.append(a + b)
                elif i == "-": 
                    stack.append(a - b)
                elif i == "*": 
                    stack.append(a*b)
                else: 
                    stack.append(int(a/b))
        return stack[0]

        
