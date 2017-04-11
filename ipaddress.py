import csv
import fileinput
from glob import glob

fnames=glob('relays*.csv')

for line in fnames:


	f=open(line,"r")
	buf=csv.reader(f)
	addresses=[]
	uniqueip=[]

	for row in buf:
		if "IP" not in row[3]:
			addresses.append(row[3])

	f.close()

	uniqueaddresses=set(addresses)
	addresses=list(uniqueaddresses)

	#print len(addresses)


	f2=open("marchipaddr2.txt","a")
	for item in addresses:
		f2.write(item)
		f2.write("\n")

	f2.close()
	
	f3=open("marchipaddr2.txt","rw+")
	ip=f3.readlines()
	for x in ip:
		if x is not ("\n"):
			uniqueip.append(x)
	uniqueipset=set(uniqueip)
	uniqueip=list(uniqueipset)
	print len(uniqueip)

	f3.truncate(0)
	for item in uniqueip:
		f3.write(item)
		

	f3.close() 
	
	
	
	
	




