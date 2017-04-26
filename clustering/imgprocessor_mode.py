#-take middle few pixels
#-or all pixels
#-remove black/white pixels

import os.path
from PIL import Image
import csv
from operator import itemgetter

#PARAMETERS
noblackwhite = True;

rootdirectory = '/Users/Keith/Dropbox/MAPS/Project'

for root,dirs,files in os.walk(rootdirectory):#insert filename here
	#print("\n")
	print ("root: ",root)
	#print ("files: ",files)
	#print("directories: ", dirs)

	file_to_open = root + '/' + "average.csv"

	f = open(file_to_open,'w')
	writer = csv.writer(f)

	for f in range (0,len(files)):
		if (files[f][-4:] == ".jpg"):
			im = Image.open(root + "/" + files[f])
			#print("\n", im.format, im.size, im.mode)
			npixels = im.size[0]*im.size[1]
			cols = im.getcolors(npixels)
			#print (cols)
			#sumRGB = [(x[0]*x[1][0], x[0]*x[1][1], x[0]*x[1][2]) for x in cols]
			
			sumRGB = []

			#for x in cols:
				#print (x)


				# if(noblackwhite == True and findmode == False):
				# 	#print (x[0]*x[1][0],x[0]*x[1][1], x[0]*x[1][2])
				# 	#if (x[1][0] != 0 & x[1][1] != 0 & x[1][2] != 0):
				# 	if (x[1][0] > 0 and x[1][1] > 0 and x[1][2] > 0): #removes black
				# 		if (x[1][0] != 255 and x[1][1] != 255 and x[1][2] != 255): 	#removes white
				# 			sumRGB.append((x[0]*x[1][0], x[0]*x[1][1], x[0]*x[1][2]))		#BUGGY. DIVIDES BY ALL. 
				# 		#print("NON BLACK PIXEL")
				
			
			mode = max(cols,key=itemgetter(0))
			pixel = (mode[1][0],mode[1][1],mode[1][2])
			writer.writerow(pixel)
			print(mode)
				
				# else:
					
				# 	sumRGB.append((x[0]*x[1][0], x[0]*x[1][1], x[0]*x[1][2]))
				
			#print(sumRGB)
			# avg = tuple([sum(x)/npixels for x in zip(*sumRGB)])
			#avg = tuple([sum(x)/len(sumRGB)/3 for x in zip(*sumRGB)])
			#print (type(avg))
			#print(avg)

			#write to csv
			# writer.writerow(avg)
			#im.show()



'''
	######COUNT OF EACH COLOR########
	for f in range (0,len(files)):
		if (files[f][-4:] == ".jpg"):
			im = Image.open(root + "/" + files[f])
			print("\n", im.format, im.size, im.mode)
			npixels = im.size[0]*im.size[1]
			cols = im.getcolors(npixels)

	################


	############COUNT OF
	for f in range (0,len(files)):
		if (files[f][-4:] == ".jpg"):
			im = Image.open(root + "/" + files[f])
			pix = im.load()
			print("\n", im.format, im.size, im.mode)
			for x in range(im.size[0]):
				for y in range(im.size[1]):
					pixel = pix[x,y]
					if pixel == 0:
						print (pixel)
			#npixels = im.size[0]*im.size[1]
			#cols = im.getcolors(npixels)
			'''