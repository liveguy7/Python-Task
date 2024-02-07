import re

line = 'jello is found in the store where lady is'
info = '2004-959-559 # this is the number'

sea = re.search(r'(nd) in (.*)', line, re.M|re.I)
m = re.match(r'jello', line, re.M|re.I)
s = re.search(r'is', line, re.M|re.I)
num = re.sub(r'#.*$', '', info)
print(num)
num = re.sub(f'\D', '', info)
print(num)

if m:
  print(m.group())

if s:
  print(s.group())

if(sea):
  print(sea.group())
else:
  print("nothing found")
