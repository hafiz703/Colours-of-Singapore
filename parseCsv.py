import csv
import os
from googlePlaces import getPhotos
from flikr import getflickrPhotos
reader = csv.reader(open('hex.csv', 'r'))
#reader = csv.reader(open('hex2.csv', 'r'))
d = []
for row in reader: 
   try:
	   temp = [float(row[0]),float(row[1])]
	   d.append(temp) 
   except:
   	 pass


for i in d:
	
	# directory = "./flickrPhotos/%s-%s"%(i[1],i[0])

	if not os.path.exists(directory):
		os.makedirs(directory)
		getflickrPhotos(i[0],i[1])
	else:
		print "exists"
	    	   

# for google photos
# for i in d:
# 	try:
# 		directory = "./GooglePhotos/%s-%s"%(i[1],i[0])
# 		if not os.path.exists(directory):
# 			os.makedirs(directory)
# 			getPhotos(i[1],i[0])
# 		else:
# 			print "exists"
# 	except:
# 		continue