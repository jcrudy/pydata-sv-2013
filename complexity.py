import pandas
from pyearth import Earth
import patsy
import numpy

data = pandas.read_csv('compare_big.csv')
#data['logn'] = numpy.log(data['n'])
data['logm'] = numpy.log(data['m'])
data = data[data['pyearth']==1]
y,X = patsy.dmatrices('time~m+n+forward_iterations+pyearth+earth+logm-1', data=data)
X = numpy.asarray(X)
#X += 0.01*numpy.random.normal(size=X.shape)
y = numpy.asarray(y)
y = y.reshape(y[:,0].shape)
#print X[0:10,:]
#print X.shape
#print y.shape
model = Earth(max_degree=5,max_terms=50,thresh=0.0001,penalty=4,linvars=['m','n','forward_iterations','pyearth','earth','logm'],xlabels=['m','n','forward_iterations','pyearth','earth','logm']).fit(X,y)

print model.trace()
print model
