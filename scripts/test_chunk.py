import pandas as pd
import time
csv_url = '/Users/derekzhang/Library/Application Support/Google/DriveFS/ZHpoYW5nMjFAdGVycG1haWwudW1kLmVkdQ/content_cache/d33/d150/301'
pos = 0
t = time.process_time()
for chunk in pd.read_csv(csv_url, header=0, usecols=['frame_id'], chunksize=200000):#, dtype={'frame_id': object}):
	print(pos)
	pos += 1
	# if pos > 50:
		# break
print(time.process_time() - t)