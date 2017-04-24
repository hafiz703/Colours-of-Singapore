import os

files = folders = 0

for _, dirnames, filenames in os.walk("./flickrPhotos"):  
    files += len(filenames)
    folders += len(dirnames)

print "{:,} files, {:,} folders".format(files, folders)