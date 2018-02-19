import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_csv("ign.csv")
df2=pd.read_csv("ign_score.csv")
df1.drop(df1.columns[7], axis=1, inplace=True)
#1
merge=df1.merge(df2,on="id")
print "The merged list headers"
print(str(list(merge)))
#2
score=list(merge["score"])
sscore=sorted(score,key=None,reverse=True)
sscore=sscore[:10]
title=list(merge["title"])
l=len(score)
st=[];i=0
print "Top 10 Movies"
for i in range(0,10,1):
  for j in range(0,l,1):
    if(score[j]==sscore[i] and title[j] not in st):
           st.append(title[j])
           break

print st
#3
movie = merge.groupby('title').score.mean().sort_values(ascending=False)
print(movie)
#4
plt.hist(merge["genre"],bins=20)
plt.show()
#5
print "Highest genre"
gen = merge.groupby('genre').score.mean().sort_values(ascending=False)
print(gen.head(1))
#6

table = pd.pivot_table(merge, values='score', index=['genre', 'title'])
print(table)






