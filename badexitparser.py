import csv


f=open("relays-2017-03-22-00-00-00.csv","r")
buf=csv.reader(f)
addresses=[]

for row in buf:
	if "E" in row[2]:
		 addresses.append(row[3])

f.close()

uniqueaddresses=set(addresses)
addresses=list(uniqueaddresses)

print len(addresses)

'''f2=open("exit.csv","a")
writeexit=csv.writer=(f2)
writeexit.writerows(addresses)

f2.close()'''



f2=open("exit.txt","a")
for item in addresses:
	f2.write(item)
	f2.write("\n")

f2.close()


