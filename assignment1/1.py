import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#1
iris=pd.read_csv("Iris.csv",index_col=0)
#2
print "headers"
headers=list(iris)
print headers
#3
print "Features"
features=headers[1:5]
print features
#4
print "First five record of iris"
print iris.loc[0:5]

sl=list(iris["SepalLengthCm"])
sw=list(iris["SepalWidthCm"])
pl=list(iris["PetalLengthCm"])
pw=list(iris["PetalWidthCm"])
#5
plt.scatter(sl,sw)
plt.title("Sepal Features")
plt.xlabel("SepalLengthCm")
plt.ylabel("SepalWidthCm")
plt.show()
plt.clf()

plt.scatter(pl,pw)
plt.title("Petal Features")
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.show()
plt.clf()
#6
print ("SepalLengthCm range:"+str(min(sl))+"-"+str(max(sl)))

sortedsl=sorted(sl,key=None,reverse=False)
n=-2

if sortedsl[-1] != sortedsl[n]:
 print ("Second larget value of SepalLengthCm is "+str(sortedsl[n]))
else:
 n=n-1
#7
nsw=np.array(sw)
print "Mean value of SepalWidthCm is "+str(np.mean(nsw[:]))
#8
l=len(sl)
Len=[]
for i in range(0,l,1):
 if sl[i]>=5:
  Len.append("Large")
 else:
  Len.append("Small")
iris["Length"]=Len
#9
sp=list(iris["Species"])
plt.hist(sp,6)
plt.title("Species")
plt.show()
plt.clf()


nsl=np.array(sl)
npl=np.array(pl)
npw=np.array(pw)
#10
print ("Standard Diviation of Sepal Length "+str(np.std(nsl[:])))

#11
head= ["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]
print "corelation"
l=iris.corr(method='pearson', min_periods=1)
print l
nl=np.array(l)
print"Columns with greater than 70% corelation"
for i in range(0,4,1):
 for j in range(0,4,1):
  if abs(nl[i][j])>0.7 :
   print"(" +str(head[i])+","+str(head[j])+")"
#12
print(iris.isnull())
#13
iris.to_csv("out.csv",sep=',')
