from geoip import geolite2

content=open("consensus.txt","r")
contentlines=content.readlines()
iplist=[]
countrylist=[]

for index,line in enumerate(contentlines):
	values=[]
	values2=[]
	if "v Tor" in line:
		values=contentlines[index-2].split(" ")
		if (values[0]=='r'):
			#print values[6]
			iplist.append(values[6])
		elif (values[0]=='a'):
			values2=contentlines[index-3].split(" ")
			#print values2[6]
			iplist.append(values2[6])

print iplist
print len(iplist)

for ip in iplist:
	match=geolite2.lookup(ip)
	if(match is not None):
		countrylist.append(match.country)

print len(countrylist)
	
