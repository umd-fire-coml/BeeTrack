import sys

assert len(sys.argv) == 2

content = None
with open(sys.argv[1]) as file:
	content = file.readlines()

import re

def m_extract(reObj):
	i=0
	for line in content:
		m = reObj.match(line)
		if m:
			#print('Match found: ', m.groups()[0])
			print(m.groups()[0])
			i+=1
	print(i)

p2 = r'.*s/step - loss: (\d\.\d*)\s'#.*val_loss: (\d\.\d*)\s'
p = re.compile(p2, re.IGNORECASE)#('.*val\\_loss: (\\d\\.\\d*)\\s', re.IGNORECASE)
print('train losses:')
m_extract(p)

p2 = r'.*val_loss: (\d\.\d*)\s'
p = re.compile(p2, re.IGNORECASE)
print('val losses:')
m_extract(p)
