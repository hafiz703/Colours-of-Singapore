#-take middle few pixels
#-or all pixels
#-remove black/white pixels

import os.path
from PIL import Image
import csv



rootdirectory = 'C:/Users/-/Desktop/PyScripts/GooglePhotos'

for root,dirs,files in os.walk(rootdirectory):#insert filename here
	print("\n")
	print ("root: ",root)
	print ("files: ",files)
	print("directories: ", dirs)

	file_to_open = root + '/' + "average.csv"

	f = open(file_to_open,'w')
	writer = csv.writer(f)

	for f in range (0,len(files)):
		if (files[f][-4:] == ".jpg"):
			im = Image.open(root + "/" + files[f])
			print("\n", im.format, im.size, im.mode)
			npixels = im.size[0]*im.size[1]
			cols = im.getcolors(npixels)
			#print (cols)
			#sumRGB = [(x[0]*x[1][0], x[0]*x[1][1], x[0]*x[1][2]) for x in cols]
			
			sumRGB = []

			for x in cols:
				sumRGB.append((x[0]*x[1][0], x[0]*x[1][1], x[0]*x[1][2]))

			avg = tuple([sum(x)/npixels for x in zip(*sumRGB)])
			print (type(avg))

			#write to csv
			writer.writerow(avg)
			#im.show()


# rootdirectory = 'D:\Documents\Maps'

rootCSV = rootdirectory + '/' + "average.csv"

## Open up a writer in root for writing csv in root
## Overriding newline as blank to remove blank entries written
with open(rootCSV, 'w') as rootF:
	rootWriter = csv.writer(rootF)
	rootWriter.writerow(['R','G','B','Lat','Lon'])

	for root,dirs,files in os.walk(rootdirectory):#insert filename here
		print("\n")
		print ("root: ",root)
		print ("files: ",files)
		print("directories: ", dirs)

		## Only open CSV that are not in rootdir 
		if (root != rootdirectory):
			file_to_open = root + '/' + "average.csv"
			print("Opening: " + file_to_open)

			with open(file_to_open, 'r') as f:
			    reader = csv.reader(f)
			    colors = [0.0,0.0,0.0];
			    #initialize count for number of valid entries in csv
			    validRowsCount = 0
			    for row in reader:
			    	if (len(row) != 0):
			    		# print('Reading row:',end='')
			    		print(row)
			    		#Increment count for each entry
			    		validRowsCount+=1
			    		for index,color in enumerate(row):
			    			colors[index] += float(color)

			    # get dir name from last part of path name
			    dirName = root.split("\\")[-1]
			    # split dir name into lat & lon
			    latLonList = dirName.split('-')

			    if (validRowsCount == 0):
			    	rootWriter.writerow([0,0,0,latLonList[0],latLonList[1]])
			    	continue;

			    for index,color in enumerate(colors):
			    	colors[index] = float(color/validRowsCount)
			    
			    # append 2 cols: lat & lon
			    for coor in latLonList:
			    	colors.append(coor)
			    # write color, lat and lon
			    # print('Writing row:',end='')
			    print(colors)
			    rootWriter.writerow(colors)