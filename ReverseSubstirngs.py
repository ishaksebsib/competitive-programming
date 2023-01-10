class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        for i in s:
            if i == '(':
                stack.append('')
            elif i == ')':
                plus = stack.pop()[::-1]
                stack[-1] += plus
            else:
                stack[-1] += i
        return stack.pop()
