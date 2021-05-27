# Example Input
# {"data":"key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"}

# Example Output
# 2


import requests
import numpy as np
import pandas as pd

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
data = r.json()['data'].split(',')
count = 0
for i in data:
  s = i.split('=')
  if s[0].strip() == 'age' and int(s[1]) >= 50:
    count  = count + 1
print(count)