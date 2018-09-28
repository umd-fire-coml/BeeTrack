# @author Derek Zhang
# DO NOT USE THIS. HIGHLY INEFFICIENT CODE
# SEE analysis2.py

import pandas as pd

csv_url = "/Volumes/GoogleDrive/My Drive/public/data_sample_release.csv"
#/Users/derekzhang/Library/Application Support/Google/DriveFS/ZHpoYW5nMjFAdGVycG1haWwudW1kLmVkdQ/content_cache/d33/d150

frame_set = set()
track_set = set()
bee_set = set()
for chunk in pd.read_csv(csv_url, chunksize=1024):
	no_imitation = pd.unique(chunk.iloc[:, 1])
	# print(no_imitation)
	frame_set = frame_set.union(no_imitation)
	no_imitation = pd.unique(chunk.iloc[:, 2])
	track_set = track_set.union(no_imitation)
	no_imitation = pd.unique(chunk.iloc[:, 6])
	bee_set = bee_set.union(no_imitation)
print(frame_set)
print(track_set)
print(bee_set)
# chunkIter = pd.read_csv(csv_url, chunksize=1024)
# df = next(chunkIter)
# frame_ids = pd.unique(df.iloc[:, 1])
# print(len(frame_ids))
# mySet = set()
# mySet = mySet.union(frame_ids)
# print(mySet)