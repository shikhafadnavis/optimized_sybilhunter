import glob
import csv
from tqdm import tqdm
import pandas as pd

f=open("topIPs","r")
buf=f.readlines()


for ip in buf:
	fingerlist=[]
	for filename in tqdm(glob.glob('relays-*.csv')):
		pdcsv = pd.read_csv(filename)
		x=pdcsv.shape[0]
		for i in range(x):
			sampleip=pdcsv.at[i,'IP']+'\n'
			if sampleip == str(ip):
				fingerlist.append(pdcsv.at[i,'Fingerprint'])
	print len(set(fingerlist))
	print set(fingerlist)

f.close()	


	




