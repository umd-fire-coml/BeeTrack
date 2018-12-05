content = None
with open('/Volumes/RAM_Disk/training_results.txt') as file:
	content = file.readlines()
import re
p2 = r'.*s/step - loss: (\d\.\d*)\s'#.*val_loss: (\d\.\d*)\s'
p = re.compile(p2, re.IGNORECASE)#('.*val\\_loss: (\\d\\.\\d*)\\s', re.IGNORECASE)
i=0
for line in content:
	m = p.match(line)
	if m:
		#print('Match found: ', m.groups()[0])
		print(m.groups()[0])
		i+=1
print(i)