import numpy as np
import random
def arr(n):
 a=[]
 for i in range(0,n,1):
  a.append([])
  for j in range(0,n,1):
    a[i].append(i+j)
 print np.array(a)

def logarr():
 l=[]
 for i in range(1,20,2):
  l.append(i)
 narr=np.array(l)
 print "2.numpy array with odd elements less than 20"
 print narr
 na1=narr[0:5]
 na2=narr[5:10]
 nmat=np.row_stack((na1,na2))
 print "The odd elements in 2*5 matrix form"
 print nmat
 print "The log of the elements"
 print np.log10(nmat)


def random1(n):
 a=[]
 for i in range(0,n,1):
  a.append([])
  for j in range(0,n,1):
    a[i].append(random.random()) 
 n_a=np.array(a)
 print "Random n*n array";print n_a 
 avg=[]
 for i in range(0,n,1):
  avg.append(np.mean(n_a[i,:]))
 print "average";print avg
 for i in range(0,n,1):
  for j in range(0,n,1):
   a[i][j]=avg[i]-a[i][j]
 n_a=np.array(a)
 print "difference"
 print n_a

def random2(n):
  a=[]
  for i in range(0,n,1):
   a.append([])
   for j in range(0,n,1):
     a[i].append(random.randint(1,100)) 
  l=[]
  for i in range(0,n,1):
    for j in range(0,n,1):
      l.append(a[i][j])
  n_a=np.array(a)
  print n_a
  print "enter target value between 1 and 100";
  v=input()
  diff=[]
  diff.append(abs(n_a[:]-v))
  #print diff
  nd=np.array(diff)
  mini=np.argmin(nd)
  print "Nearet value"
  print l[mini]

def fun1():
 print "enter size of array 1"
 n1=input()
 a=[];b=[]
 for i in range(0,n1,1):
  a.append(random.random())
 print "enter size of array2"
 n2=input()
 for i in range(0,n1,1):
  b.append(random.random())
 if(a==b):
   print "arrays are equal"
 else:
   print"Arrays are not equal"

def fun2():
 print "enter size of array "
 n1=input()
 a=[]
 for i in range(0,n1,1):
  a.append(random.random())   
 print a
 print "enter value of n"
 n=input()
 a=sorted(a,key=None,reverse=True)
 print a[:n]

print"1.Array with elements i+j";print "enter value of n"
n=input()
arr(n)
logarr()
print "3.random array and mean";print "enter value of n"
n=input()
random1(n)
print "4.random array and nearest value";print "enter value of n"
n=input()
random2(n)
print "5.random arrays equal or not"
fun1()
print "6.n largest values of an array"
fun2()
