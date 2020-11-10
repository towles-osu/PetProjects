#auth0r: Stew
#This is some functions that are helpful for the discrete math class I'm taking

def permut(n, k):
  """this calculates k-permutations of n objects"""
  answer = 1
  for i in range(n,n-k,-1):
    answer = answer * i
  return answer
  
def combin(n, k):
  """this calculates k-combinations of n objects"""
  answer = 1
  for i in range(n, n-k, -1):
    answer = answer * i
  for i_2 in range(k,0,-1):
    answer = answer / i_2
  return answer

def find_bin_term(n,k):

# print(permut(5,3))
# print(combin(5,3))