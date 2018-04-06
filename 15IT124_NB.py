import random
import math


file=open("dataset.csv","r")
b=[]
i=0
flag=0
for x in file:
	if flag==0:
		flag=1
	else:
		a=x.split(",")
		b.append(a)
		if b[i][18] == "yes\n":
			b[i][18] = 1
		else:
			b[i][18] = 0
		i+=1

n=i-1
pyes=pno=0.0
for x in range(50):
	if b[x][18]==1:
		pyes=pyes+1
	else:
		pno=pno+1
pyes/=50
pno/=50

mean=[]

for i in range(18):
	a=[]
	t1=t2=0.0
	for j in range(50):
		if b[j][18]==1:
			t1+=float(b[j][i])/25
		else:
			t2+=float(b[j][i])/25
	a.append(t1)
	a.append(t2)
	mean.append(a)

# for i in range(18):
# 	print mean[i]

sig=[]
for i in range(18):
	a=[]
	t1=t2=0.0
	for j in range(50):
		if b[j][18]==1:
			t1+=(float(b[j][i])-mean[i][0])*(float(b[j][i])-mean[i][0])/25
		else:
			t2+=(float(b[j][i])-mean[i][1])*(float(b[j][i])-mean[i][1])/25
	a.append(t1)
	a.append(t2)
	sig.append(a)

# for i in range(18):
# 	print sig[i]

def nb(chrom):
	acc=0.0
	for i in range(50,60):
		yes=pyes
		no=pno
		for k in range(18):
			if chrom[k]==1:
				yes*=math.exp(-((float(b[i][k])-mean[k][0])**2)/(2*sig[k][0]))/(2.5066*sig[k][0]**0.5)
				no*=math.exp(-((float(b[i][k])-mean[k][1])**2)/(2*sig[k][1]))/(2.5066*sig[k][1]**0.5)
		if (yes>=no and b[i][18]==1) or (yes<no and b[i][18]==0):
			acc+=1
		if yes>=no:
			print "Not Malicious"
		else:
			print "Malicious"

	print "Accuracy :",acc/10

print "Enter selected feature list :",
nb(input())