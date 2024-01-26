# write here
def del_char(s, c):
  if len(c) != 1:
    return s
  news = ""
  for ch in s:
    if ch != c:
      news += ch
  return news

# Can also use the replace(string, character) function
# s.replace(c, '')

# suffix code
s = input()
c = input()
print(del_char(s, c))
