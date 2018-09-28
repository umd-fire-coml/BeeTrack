# @author Derek Zhang
# Finds all the unique frame IDs, track IDs, and bee IDs.
# So I just remembered update is a thing
# yes this is much better

import pandas as pd

csv_url = "/Users/derekzhang/Library/Application Support/Google/DriveFS/ZHpoYW5nMjFAdGVycG1haWwudW1kLmVkdQ/content_cache/d33/d150/301"
# csv_url = "test.csv"

frame_set = set()
track_set = set()
bee_set = set()
# pos = 0
# no_imitation = pd.unique(chunk.iloc[:, 0])
# no_imitation = pd.unique(chunk.iloc[:, 1])
# no_imitation = pd.unique(chunk.iloc[:, 2])
# print(chunk.dtypes)
	# print(pos)
	# pos += 1
for chunk in pd.read_csv(csv_url, header=0, usecols=["frame_id", "track_id", "bee_id"], chunksize=200000):
	frame_set.update(chunk.iloc[:, 0])
	track_set.update(chunk.iloc[:, 1])
	bee_set.update(chunk.iloc[:, 2])
print(len(frame_set))
print(len(track_set))
print(len(bee_set))
print(frame_set)
print(track_set)
print(bee_set)