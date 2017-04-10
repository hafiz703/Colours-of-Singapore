# base = "http://localhost:5000/search/?q="
# query = input('Enter query: ')
# for word in query.split():
# 	if(query.split().index(word)!=len(query.split())-1):
# 		word += "+"		
# 	base+=word

# print(base)


# def bina(x):	 
# 	ls=[]
# 	res = ""	 
# 	while x!=0:		 
# 		i = -1
# 		res = 2**i		
# 		while res<=x:			 		 
# 			i+=1
# 			res = 2**i
# 		i-=1
# 		res = 2**i
# 		ls.append(i)		 
# 		x-=res
# 	resList = ["1" if i in ls else "0" for i in range(ls[0]+1)][::-1] 
# 	res = ''.join(resList)	
# 	return res 

# print(bina(2))
 


# a,b = 0,1
# for x in range(100):
#     print(a)
#     a=b
#     b=a+b


# def classic_fibo(n):
# 	if(n<=1):
# 		return n 
# 	else:
# 		return classic_fibo(n-1) + classic_fibo(n-2)
 
 
 


# dic = {0:0,1:1}
# def fast_fibo(n):
# 	global dic		 
# 	if(n not in dic.keys()):		 
# 		dic[n] = fast_fibo(n-1)+fast_fibo(n-2)			
		 
# 	return dic[n]
 
# print(fast_fibo(8))
 


def checkDupe(ls,k):
	res = []
	while k in ls:
		# print(res)
		res.append(ls.index(k))
		ls[ls.index(k)] = '#'
	return res



def countryLeader(ls):
	res = []
	for word in ls:
		dic = {}
		for letter in word:
			dic[letter] =0
		res.append(len(dic))
	# print(res)
	maxUnique = max(res)
	index = res.index(maxUnique)
	indexList = checkDupe(res,maxUnique)
	if(len(indexList)==1):
		return ls[index]
	else:
		tieList = [ls[j] for j in indexList]
		indexMinimum = tieList.index(min(tieList))
		return ls[indexList[indexMinimum]] 
		

 
with open("in3.in") as f:
    lines = f.read().splitlines() 

lines.append('1')

numCases = int(lines[0])

testList = list()
temp = list()
for i in range(2,len(lines)):	 
	try:		 
		int(lines[i])
		testList.append(temp)
		temp = list()
	except ValueError:		
		temp.append(lines[i])


for i in testList:
	print("Case #%d"%(testList.index(i)+1) +": " +countryLeader(i))
# print(testList)






 
 