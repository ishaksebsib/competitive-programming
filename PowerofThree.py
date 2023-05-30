

'''
1. create a funciton that accept an integer
2. if it is less or equal to 0 return False
3. if 1162261467 % n equls to 0 return True  .. because The maximum power of 3 value that integer can hold is 1162261467 ( 3^19 )
4. otherwise return False

'''
  
def powerofThree(n):
  if n <= 0 :
    return False
  elif 1162261467 % n == 0:
    return True
  else:
    return False
