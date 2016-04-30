import numpy as np
import itertools
import sklearn
from sklearn.multiclass import OneVsOneClassifier
from sklearn import svm
from sklearn.externals import joblib
from sklearn import ensemble
#fp=open("./trainingset.txt",'r')
X=[]
y=[]
''' for line in fp:
	x=[]
	line=line.split(",")
#	print line
	for i in xrange(0,len(line)-1):
		x.append(float(line[i]))
	X.append(x)
	if line[len(line)-1].strip("\n")=='Yes':
		y.append(1.0)
	else:
		y.append(0.0) '''

#	print X
#	print y   
dataset = np.loadtxt("./finaltt.txt", delimiter=",")
#print X
#Xx=np.array(X)
X=dataset[:,0:67]
y=dataset[:,71]
print y
clf = sklearn.ensemble.RandomForestClassifier(random_state=None)
#clf = OneVsOneClassifier(svm.SVC(kernel='rbf'))
clf.fit(X,y)
#joblib.dump(clf, 'my_model_rbf.pkl', compress=9)
print "Model Loaded"
###  Testing 

testset = np.loadtxt("./finaltest.txt", delimiter=",")
X=testset[:,0:67]
y=testset[:,71]
b=clf.predict(X)
true=0
false=0
tt = 0
ff = 0
tp = 0
fn = 0
for i,j in itertools.izip(b,y):
	print i,":",j
	if i==1.0:
		tt = tt + 1
	if i == 0.0:
	        ff = ff + 1
	if i==j:
		true=true+1
	        if i == 1.0:
	        	tp = tp + 1
	        else:
	                fn = fn + 1
	else:
		false=false+1
acc = (true * 100) /(true+false)
#print "Accuracy:", acc,"%"
print true," ",false
print "Accuracy:", acc,"%"
#print tt," ",ff
#print tp," ",fn
print "Confusion Matrix :"
print tp," ",tt-tp
print ff-fn," ",fn

