#!/usr/bin/python3
import sys
import os
import pandas as pd
def get_size(path):
	total = 0
	for entry in os.scandir(path):
		try:
			if entry.is_dir(follow_symlinks=False):
				total += get_size(entry.path)
			else:
				total += entry.stat(follow_symlinks=False).st_size
		except Exception as e:
			print(f"Exception : {e}")
			total += 0
	return total

if __name__=='__main__':
	path = '/home'
	dir = sys.argv[1] if len(sys.argv)>1 else path
	usage=[]
	paths=[]
	for entry in os.scandir(dir):
		if (entry.is_dir(follow_symlinks=False)):
			total=get_size(entry.path)/(1024*1024)
			#print(entry.path,total)
			paths.append(entry.path)
			usage.append(total)
	usage_dict = {'Directory':paths,'Usage(Mb)':usage}
	df=pd.DataFrame(usage_dict)
	df.to_csv("DiskReport.csv")
