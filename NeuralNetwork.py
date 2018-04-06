import numpy as np
import math
import random

print "Enter learning rate :",
l=input()

print "Enter selected feature list :",
chrom=input()

def sigmoid(s):
	if s <= -700:
		return 0
	res=1/(1+math.exp(-s))
	return res

file=open("dataset.csv","r")
a=[]
i=-1
for x in file:
	if i < 0:
		i+=1
	else:
		(b)=x.split(",")
		a.append(b)
		if a[i][18] == "yes\n":
			a[i][18] = 1
		else:
			a[i][18] = 0
		i+=1

for i in range(60):
	for j in xrange(18):
		a[i][j]=float(a[i][j])

actual_class=[]
for i in range(60):
	actual_class.append(a[i].pop(18))

for i in range(17,-1,-1):
	if chrom[i]==0:
		for j in range(60):
			a[j].pop(i)

for i in xrange(60):
	print a[i]

# Data set complete
# 9 nodes in hidden layer
leng=0
for i in range(18):
	if chrom[i]==1:
		leng+=1

w=[]
for i in range(9):
	temp=[]
	for j in range(leng):
		temp.append(1.0*random.randint(-100,100)/100)
	w.append(temp)
print w
wo=[]
for i in range(9):
	wo.append(1.0*random.randint(-100,100)/100)

b=[]
for i in range(9):
	b.append(1.0*random.randint(-100,100)/100)
	
bo=1.0*random.randint(-100,100)/100

err=[]
for i in range(9):
	err.append(0)

for count in range(170):
	for x in range(60):
		if x%5 != count%5:
			o= np.dot(w,a[x])+b
			for i in range(9):
				o[i]= sigmoid(o[i])

			o1=sigmoid(np.dot(wo,o)+bo)
			
			e=o1*(1-o1)*(actual_class[x]-o1)

			for i in range(9):
				err[i]=o[i]*(1-o[i])*e*wo[i]

			for i in range(9):
				wo[i]+=l*e*o[i]

			for i in range(9):
				for j in range(leng):
					w[i][j]+=l*err[i]*a[x][j]

			bo+=l*e

			for i in range(9):
				b[i]+=l*err[i]
	for x in range(60):
		if x%5 == count%5:
			o= np.dot(w,a[x])+b
			for i in range(9):
				o[i]= sigmoid(o[i])

			o1=sigmoid(np.dot(wo,o)+bo)
			if o1<0.5:
				ans=0
			else:
				ans=1
			print ans,actual_class[x],o1
	print

#RESULTS
tp=tn=fp=fn=0
rmse=0.0
for x in range(60):
	o=np.dot(w,a[x])+b
	for i in range(9):
		o[i]=sigmoid(o[i])
	o1=sigmoid(np.dot(wo,o)+bo)
	if o1 >= 0.5 and actual_class[x]==1:
		tp+=1
	if o1 >= 0.5 and actual_class[x]==0:
		fp+=1
		rmse+=1
	if o1 < 0.5 and actual_class[x]==0:
		tn+=1
	if o1 < 0.5 and actual_class[x]==1:
		fn+=1
		rmse+=1

rmse=1.0*(rmse/300)**0.5
print tp,fp
print tn,fn

print "Learning rate",l
print "Precision",1.0*tp/(tp+fp)
print "Recall",1.0*tp/(tp+fn)
print "F-Measure",2.0*tp/(2*tp+fp+fn)
print "RMSE",rmse