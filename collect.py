import re

print('. - any character before o')
match = re.search(r'.o', 'Jello World')
if(match):
  print('found', match.group())
else:
  print('not found')

match = re.search(r'^.', 'jello123jello')
if(match):
  print('found', match.group())
else:
  print('not found')

match = re.search(r'.$', 'jello123jello')
if(match):
  print('found', match.group())
else:
  print('not found')