import csv
from googlePlaces import getPhotos
reader = csv.reader(open('hex.csv', 'r'))
d = []
for row in reader:
   # k, v = row
   # print len(row)
   try:
	   temp = [float(row[0]),float(row[1])]
	   d.append(temp) 
   except:
   	 pass
	   


# print d
for i in d:
	try:
		directory = "./GooglePhotos/%s-%s"%(i[1],i[0])
		if not os.path.exists(directory):
			os.makedirs(directory)
			getPhotos(i[1],i[0])
		else:
			print "exists"
	except:
		continue