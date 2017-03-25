from geoip import geolite2
from collections import defaultdict

#opening and reading a consensus file into a buffer
content=open("consensus.txt","r")
contentlines=content.readlines()

#list of all IP addresses in a context file
iplist=[]
#list of countries
countrylist=[]
#list of concatenated strings (IP address)+(ports)+(two-character country code)
relayinfo=[]

#seedrelay string
seedrelay='37.221.171.23490040DE'

levendict=defaultdict(int)

def levenshtein_distance(first, second):
    """Find the Levenshtein distance between two strings."""
    if len(first) > len(second):
        first, second = second, first
    if len(second) == 0:
        return len(first)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [[0] * second_length for x in range(first_length)]
    for i in range(first_length):
       distance_matrix[i][0] = i
    for j in range(second_length):
       distance_matrix[0][j]=j
    for i in xrange(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
    return distance_matrix[first_length-1][second_length-1]

for index,line in enumerate(contentlines):
	values=[]
	values2=[]
	if "v Tor" in line:
		values=contentlines[index-2].split(" ")
		if (values[0]=='r'):
			#print values[6]
			iplist.append(values[6])
			ip=values[6]
			port=values[7]+values[8]
		elif (values[0]=='a'):
			values2=contentlines[index-3].split(" ")
			#print values2[6]
			iplist.append(values2[6])
			ip=values2[6]
			port=values2[7]+values2[8]
		
		match=geolite2.lookup(ip)
		if(match is not None):
			countrylist.append(match.country)
			if (match.country is not None):
				item=ip+port+match.country
				relayinfo.append(item)
				levendist=levenshtein_distance(seedrelay,item)
				levendict[ip]=levendist
				






sorted(levendict.items(), key=lambda x: x[1])

print dict(levendict)




	






	
