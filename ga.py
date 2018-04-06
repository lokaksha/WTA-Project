import random
import math

def check(fit):
	for i in range(30):
		if fit[i]!=1:
			return 0
	return 1

file=open("dataset.csv","r")
b=[]
flag=0
i=0
for x in file:
	if flag == 0:
		flag = 1
	else:
		(a)=x.split(",")
		b.append(a)
		if b[i][18] == "yes\n":
			b[i][18] = 1
		else:
			b[i][18] = 0
		print b[i]
		i+=1


pyes=0.0
pno=0.0
for i in range(50):
	if b[i][18] == 1:
		pyes+=1
	else:
		pno+=1

pyes=pyes/50
pno=pno/50

sig=[]
mean=[]
for i in range(18):
	a=[]
	x=0.0
	y=0.0
	for j in range(50):
		if b[j][18]==1:
			x+=float(b[j][i])/25
		else:
			y+=float(b[j][i])/25
	a.append(x)
	a.append(y)
	mean.append(a)

x=0.0
y=0.0
for i in range(18):
	a=[]
	x=0.0
	y=0.0
	for j in range(50):
		if b[j][18]==1:
			x+=(float(b[j][i])-mean[i][0])*(float(b[j][i])-mean[i][0])/25
		else:
			y+=(float(b[j][i])-mean[i][1])*(float(b[j][i])-mean[i][1])/25
	a.append(x)
	a.append(y)
	sig.append(a)
for i in range(18):
	print i,sig[i]

def nb(chrom):
	acc=0.0
	for i in range(50,60):
		yes=pyes
		no=pno
		for k in range(18):
			if chrom[k]==1:
				yes*=math.exp(-((float(b[i][k])-mean[k][0])**2)/(2*sig[k][0]))/(2.5066*sig[k][0]**0.5)
				no*=math.exp(-((float(b[i][k])-mean[k][1])**2)/(2*sig[k][1]))/(2.5066*sig[k][1]**0.5)
		print yes,no,b[i][18]
		if (yes>=no and b[i][18]==1) or (yes<no and b[i][18]==0):
			acc+=1
	return acc/10





#INITIALIZE POPULATION
chrom=[]
for i in range(30):
	a=[]
	for j in range(18):
		a.append(random.randint(0,1))
	chrom.append(a)

temp=list(chrom)

fit=[]
for i in range(30):
	fit.append(0)

prob=[]
for i in range(30):
	prob.append(0)

cross=[0,0,0,0,0,0,0]

count=1

while check(fit)==0:
	print count
	count+=1
	#FITNESS
	for i in range(30):
		fit[i]=nb(chrom[i])
		print fit[i]
	
	print ""

	#SELECTION
	total=0
	for i in range(30):
		total+=fit[i]

	for i in range(30):
		prob[i]=float(fit[i])/total

	for i in range(1,30):
		prob[i]+=prob[i-1]
	#	print prob[i]
	for i in range(30):
		rand=random.uniform(0,1)
		if rand < prob[0]:
			temp[i]=chrom[0]
		for j in range(1,30):
			if rand < prob[j] and rand > prob[j-1]:
				temp[i]=chrom[j]

	chrom=list(temp)

	#CROSSOVER
	for i in range(7):
		cross[i]=random.randint(0,29)

	for i in range(7):
		rand1=random.randint(1,43)
		rand2=i
		while rand2==i:
			rand2=random.randint(0,6)
		for j in range(rand1,18):
			temp[cross[i]][j]=chrom[cross[rand2]][j]

	chrom=list(temp)

	#MUTATION
	for i in range(3):
		rand1=random.randint(0,29)
		rand2=random.randint(0,17)
		if chrom[rand1][rand2] == 0:
			chrom[rand1][rand2]=1
		else:
			chrom[rand1][rand2]=0

print chrom