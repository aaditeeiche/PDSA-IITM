# Write code here
def shuffle(l1, l2):
  res = []
  limit = min(len(l1), len(l2))
  for i in range(limit):
    res.append(l1[i])
    res.append(l2[i])

  if (len(l1) > len(l2)):
    res += l1[limit:]
  else:
    res += l2[limit:]

  # if len(l1) > limit:
  #   for i in range(limit, len(l1)):
  #     res.append(l1[i])
  # else:
  #   for i in range(limit, len(l2)):
  #     res.append(l2[i])
  return res


# suffix Code
L1 = eval(input())
L2 = eval(input())
print(shuffle(L1, L2))
