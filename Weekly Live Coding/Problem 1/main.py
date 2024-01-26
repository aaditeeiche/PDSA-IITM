# write here
def primeproduct(m):
  if m < 0:
    return False
  
  primefact = []
  # Calculate all factors
  for i in range (2,m,1): # exclude first and last factor
    if m%i == 0:
      # Check if factor is prime or not
      check = 0
      for k in range(2,i,1): 
        if i%k == 0:
          check += 1
      if check == 0: # If prime factor, append to list
        primefact.append(i)
  # print(primefact)

  # Bruteforce - Check Prime Products
  for a in primefact:
    for b in primefact:
      if a * b == m:
        return True
  return False  

#Suffix Code
n = int(input())
print(primeproduct(n))