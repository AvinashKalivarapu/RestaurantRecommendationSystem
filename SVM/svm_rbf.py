import numpy as np
import itertools
from sklearn.multiclass import OneVsOneClassifier
from sklearn import svm
from sklearn.externals import joblib
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
#dataset = np.loadtxt("./finaltt.txt", delimiter=",")
#print X
#Xx=np.array(X)
#X=dataset[:,0:70]
#y=dataset[:,71]
#print y
#clf = svm.LinearSVC(random_state=0)
#clf = OneVsOneClassifier(svm.SVC(kernel='rbf'))
#clf.fit(X,y)
#joblib.dump(clf, 'my_model_rbf.pkl', compress=9)
#print "Model Loaded"
###  Testing 
b = []
yy = []
k = 1
clf = joblib.load('my_model_rbf.pkl')
testset = np.loadtxt("./finaltest.txt", delimiter=",")
print "Model Loaded"
X=testset[:,0:67]
y=testset[:,71]
print "before"
for i in X:
    yy.append(i)
#   print i
    print "k-value :", k
    k = k + 1
    b.append(clf.predict(yy))
    yy = []
#yy.append(X[0])
#b = clf.predict(yy)
print "after"
true=0
false=0
for i,j in itertools.izip(b,y):
	print i[0],":",j
	if i[0]==j:
		true=true+1
	else:
		false=false+1

print true," ",false
