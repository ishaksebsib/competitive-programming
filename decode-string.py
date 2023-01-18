class Solution:
  def decodeString(self, s: str) -> str:
      stack = []; curN = 0; curS = ''
      for c in s:
          if c == '[':
              stack.append(curS)
              stack.append(curN)
              curS = ''
              curN = 0
          elif c == ']':
              num = stack.pop()
              prevString = stack.pop()
              curS = prevString + num*curS
          elif c.isdigit():
              curN = curN*10 + int(c)
          else:
              curS += c
      return curS
