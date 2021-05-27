
# Input: "3gy41d216"
# Output: true


# Input: "f09r27i8e67"
# Output: false 


import re

def EvenPairs(strParam):
  list_com = [n for n in re.split(r"([0-9]+)",strParam) if n.isnumeric()]
  for n in list_com:
    m = [1 for k in n if int(k) % 2 == 0]
    if sum(m) >=2 and int(n[-1]) % 2 == 0:
      return "true"
  return "false"
print(EvenPairs(input()))
