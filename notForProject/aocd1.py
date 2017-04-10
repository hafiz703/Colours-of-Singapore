fo = open("input.txt", "r")
inp = fo.read()
ls =inp.split()
# ls = ["R8", "R4", "R4", "R8"]
print(ls)
def getDirFace(initDir,step):
	if(initDir=="North"):
		if(step=="L"):
			return "West"
		else:
			return "East"
	elif(initDir=="West"):
		if(step=="L"):
			return "South"
		else:
			return "North"
	elif(initDir=="South"):
		if(step=="L"):
			return "East"
		else:
			return "West"
	else:
		if(step=="L"):
			return "North"
		else:
			return "South"
def checkIntersect(a,b):
	# print(a,b)
	x1 = a[0]
	y1 = a[1] 
	x2 = a[2]
	y2 = a[3]
	x3 = b[0]
	y3 = b[1]
	x4 = b[2]
	y4 = b[3]


	x12 = x2 - x1;
	x34 = x4 - x3;
	y12 = y2 - y1;
	y34 = y4 - y3;

	print([x12,y12],[x34,y34])
	try:
		if((x12==0 and x34 ==0) or (y12 ==0 and y34 ==0)):
			return False
		if(x12>x34 and x12!=0):
			n1 = x12%x34
		else:
			n1 = x34%x12
		if(y12>y34 and y12!=0):			  
			n2 = y12%y34
		else:
			n2 = y34%y12
		if (n1==0 and n2==0):
			return False
		
	except:
		return True
	return True


	
	return False

def getLines(states):
	lines = []
	for i in range(len(states)-1):		 
		j = states[i]
		k = states[i+1]
		ln = [j[0],j[1],k[0],k[1]]
		lines.append(ln)
	return lines


def main():
	dirFace = "North"
	dic = {'North':0,'East':0}
	states=[[0,0]]
	lines = []
	for i in ls:		 
		try:
			moves = int(i[1:(len(i)-1)])
		except ValueError:
			moves = int(i[1:(len(i))])
		 
		dirFace = getDirFace(dirFace,i[0])

		if (dirFace=="North" or dirFace =="East"):
			dic[dirFace]+=moves

		elif(dirFace=="South"):			
			dic["North"]-=moves
			
		elif(dirFace=="West"):			
			dic["East"]-=moves		 
				

		currentState = [dic["East"],dic["North"]]
		states.append(currentState)	
	lines = getLines(states)

	# print("kek:",checkIntersect(lines[1],lines[3]))
	print("states:",states) 
	print("lines:",lines)
	for i in range(len(lines)-1):
		j=[k for k in range(1,len(lines)) if k!=i+1]
		# print(j)
		for index in j:
			if(checkIntersect(lines[i],lines[index])):
				return(lines[i],lines[index],i,index)

		print(j)

	

	return(dic)
			 
print(main())











