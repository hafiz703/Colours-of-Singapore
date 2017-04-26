#-take middle few pixels
#-or all pixels
#-remove black/white pixels

import os.path
from PIL import Image
import csv

#PARAMETERS
noblackwhite = True;
removegreyscale = True;

rootdirectory = '/Users/Keith/Dropbox/MAPS/Project'

#CHANGE THE CROP SIZE HERE
cropsize = 100000

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
			
			centerX=im.size[0]/2
			centerY=im.size[1]/2

			#totalpixels = cropsize*cropsize
			totalpixels = 0

			sumR = 0
			sumG = 0
			sumB = 0

			if (im.size[0]>cropsize and im.size[1]>cropsize):
				topleftX = int(centerX - cropsize/2)
				topleftY = int(centerY - cropsize/2)
				rightX = topleftX + cropsize
				rightY = topleftY + cropsize
				print(topleftX,topleftY,rightX,rightY)
				for x in range(topleftX,rightX):
					for y in range(topleftY,rightY):
						pixel = im.getpixel((x,y))
						if (removegreyscale == True):
							if (abs(pixel[0]-pixel[1]) > 5 and abs(pixel[0]-pixel[2])>5 and abs(pixel[1]-pixel[2])>5): #greyscale

								sumR += pixel[0]
								sumG += pixel[1]
								sumB += pixel[2]
								totalpixels += 1
						else:
							sumR += pixel[0]
							sumG += pixel[1]
							sumB += pixel[2]
							totalpixels += 1

				if (totalpixels == 0):
					writer.writerow([0,0,0])
				else:
					averageR = sumR/totalpixels
					averageG = sumG/totalpixels
					averageB = sumB/totalpixels

					print("Average: ",averageR,averageG,averageB)
					writer.writerow([averageR,averageG,averageB])

			else: #just get all pixesls 
				sumRGB = []
				includedpixels = 0
				for x in cols:
					sumRGB.append((x[0]*x[1][0], x[0]*x[1][1], x[0]*x[1][2]))
					includedpixels += x[0]
				avg =  tuple([sum(x)/includedpixels for x in zip(*sumRGB)])
				writer.writerow(avg)

			color = im.getpixel((1,1))
			#print(color)

			#write to csv
			#writer.writerow(avg)
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