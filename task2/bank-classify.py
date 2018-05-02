import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_selection import SelectKBest, f_classif 
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
#import seaborn as sns

a=pd.read_csv("bank-full1.csv")
#print a.describe(include="all")    #checking for missing values

#sns.pairplot(a, hue='y', size=2.5) #To extract the important features
#plt.show()

labels = np.asarray(a.y)
le = LabelEncoder()
le.fit(labels)
# apply encoding to labels
labels = le.transform(labels)


df_selected = a.drop(["y","age","day","pdays","campaign"], axis=1) #dropping features based on the plot
df_features = df_selected.to_dict(orient='records')
#one hot encoding
vec = DictVectorizer()
features = vec.fit_transform(df_features).toarray()

#splitting traing and testing data
features_train, features_test, labels_train, labels_test = train_test_split( features, labels,  test_size=0.30, stratify=labels)

#splitting training and validation data
features_train, features_valid, labels_train, labels_valid = train_test_split( features_train, labels_train,  test_size=0.20)


# Random Forest
print("Random Forest classifier")
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(class_weight="balanced",n_estimators=100,)
clf.fit(features_train, labels_train)
#on valid set
acc_test = clf.score(features_valid, labels_valid)
print ("Test Accuracy on validation set:", acc_test)
pred = clf.predict(features_valid)
print("confusion matrix")
print(confusion_matrix(labels_valid, pred))
print(classification_report(labels_valid, pred))
#on test set
acc_test = clf.score(features_test, labels_test)
print ("Test Accuracy on test set:", acc_test)


#Decision Tree
print("Decision Tree classifier")
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
#on valid set
acc_test = clf.score(features_valid, labels_valid)
print ("Test Accuracy on validation set:", acc_test)
pred = clf.predict(features_valid)
print("confusion matrix")
print(confusion_matrix(labels_valid, pred))
print(classification_report(labels_valid, pred))
#on test set
acc_test = clf.score(features_test, labels_test)
print ("Test Accuracy on test set:", acc_test)


#k-Nearest Neighbours
print("K-Nearest Neighbour")
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()
clf.fit(features_train, labels_train)
#on valid set
acc_test = clf.score(features_valid, labels_valid)
print ("Test Accuracy o validation set:", acc_test)
pred = clf.predict(features_valid)
print("confusion matrix")
print(confusion_matrix(labels_valid, pred))
print(classification_report(labels_valid, pred))
#on test set
acc_test = clf.score(features_test, labels_test)
print ("Test Accuracy on test set:", acc_test)



