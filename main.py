# 1.1 Implement a recursive function to calculate the factorial of a given number
def fact _ rec(n):
  if n==0 or n==1:
    return 1
else:
  return n*fact_ rec(n-1)
  number=2
  res= fact_ rec( number)
  print(" The factorial pf {} is{}". format( number,res))