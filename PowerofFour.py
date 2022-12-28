'''
1. create a function that accept an integer
2. return False if it is 0 or less than 0
3. return True if `n` is a power of 2, and the remainder is 1 when divided by 3

'''


def checkPowerOf4(n):
    if n <= 0:
        return False
    return ((n & (n - 1)) == 0) and (n % 3 == 1)
