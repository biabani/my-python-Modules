import os

def validExt(filename,ext):
	filename = filename.lower()
	ext = ext.lower()
	i=-1
	for letter in ext[::-1]:
		if letter == filename[i]:
			i-=1
			continue 
		else:
			return False
	return True

def imageList(dir):
	fileList= []
	extNames = [".jpg",".bmp",".jpeg",".png"]
	for filename in os.listdir(dir):
		for ext in extNames:
			if validExt(filename,ext):
				fileList.append(dir+"/"+filename)
				break
	return fileList
	
