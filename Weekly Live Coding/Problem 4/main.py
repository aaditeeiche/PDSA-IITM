# write code here
def expanding(L):
  for i in range(len(L) - 2):
    if (abs(L[i] - L[i + 1]) >= abs(L[i + 1] - L[i + 2])):
      return False
  return True


# suffix code
L = eval(input())
print(expanding(L))
