# LINK : https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        if not self.min:
            self.min.append(val)
        elif val <= self.getMin():
            self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.getMin() == self.top():
            self.min.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
