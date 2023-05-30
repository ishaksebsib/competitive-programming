
def fib(n):
  if n == 0:
    return 0
  if n == 1:
      return 1
  twoback = 0
  oneback = 1
  for i in range(0, n-1):
      curr = oneback + twoback
      twoback = oneback
      oneback = curr
  return curr
