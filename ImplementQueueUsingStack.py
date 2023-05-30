class Node():
    def __init__(self,value):
        self.val = value
        self.next = None
class MyQueue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0        

    def push(self, x: int) -> None:
        newNode = Node(x)
        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

        self.length+=1
        return self
        

    def pop(self) -> int:
        if self.first  == None:
            return self
        holdPointer = self.first.val
        self.first = self.first.next
        self.length-=1
        return holdPointer

    def peek(self) -> int:
        temp = self.first
        if temp != None:
            return temp.val
        else:
            return self
        

    def empty(self) -> bool:
        if self.length == 0 :
            return True
        return False
