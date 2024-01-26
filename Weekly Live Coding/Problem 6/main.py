# write code here
def histogram(L):
  L.sort()
  print(L)

  freq = {}
  for i in L:
    if i in freq.keys():
      freq[i] += 1
    else:
      freq[i] = 1
  print(freq)

  newL = [(freq[i], i) for i in freq.keys()]
  print(newL.sort())

  finalL = [(t[1], t[0]) for t in newL]
  return finalL


# sufix code
L = eval(input())
print(histogram(L))
