'''
1. create a funciton/method that accept head of Node/linkedlist 
2. assign two variable as head
3. while there is next value run the while loop 
4. setp 2 steps for the first variable because it is same as by dividing by 2 
5. stepup 1 steps for to get the middle 
'''

def middleNode(head):
    first = head
    middle = head
    while first and first.next:
        first = first.next.next
        middle = middle.next
    return middle
