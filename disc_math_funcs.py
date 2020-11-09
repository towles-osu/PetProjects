#auth0r: Stew
#This is some functions that are helpful for the discrete math class I'm taking

def permut(n, k):
  answer = 1
  for i in range(n,k,-1):
    answer = answer * i
  return answer
  
def combin(n, k):
  answer = factorial(n) / (factorial(n-k) * factorial(k))
  return answer
