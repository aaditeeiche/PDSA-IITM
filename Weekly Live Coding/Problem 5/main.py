# write code here
def sumsquare(l):
  evensq = oddsq = 0
  for n in l:
    if n%2==0: 
      evensq += n*n
    else: 
      oddsq += n*n
  res = []
  res.append(oddsq)
  res.append(evensq)
  return res

# Suffix code
L = eval(input())
print(sumsquare(L))