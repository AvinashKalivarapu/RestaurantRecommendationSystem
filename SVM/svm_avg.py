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
dataset = np.loadtxt("./finaltt.txt", delimiter=",")
#print X
#Xx=np.array(X)
X=dataset[:,0:70]
y=dataset[:,71]
print y
clf = svm.LinearSVC(random_state=0)
#clf = OneVsOneClassifier(svm.SVC(kernel='rbf'))
clf.fit(X,y)
#joblib.dump(clf, 'my_model_rbf.pkl', compress=9)
print "Model Loaded"
###  Testing 
avg=[3.79718245818,1.10638377562,1.467269791]
testset = np.loadtxt("./finaltest.txt", delimiter=",")
XX=[]
yy=[]
X=testset[:,0:70]
kk=0
for i in X:
	kk=kk+1
	i=list(i)
	if kk>14369:
		i=i[0:67]
		i.extend(avg)
	i=np.array(i)
	XX.append(i)

y=testset[:,71]
b=clf.predict(XX)
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
