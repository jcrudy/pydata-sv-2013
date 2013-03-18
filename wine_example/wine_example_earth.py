'''
Created on Mar 13, 2013

@author: jasonrudy
'''


import pandas
import pyearth
import patsy
import numpy
numpy.random.seed(0)

white = pandas.read_csv('winequality-white.csv',sep=';')
red = pandas.read_csv('winequality-white.csv',sep=';')
white['red'] = [0]*white.shape[0]
red['red'] = [1]*red.shape[0]
data = pandas.concat([white,red])
data['testing'] = numpy.random.binomial(1,0.3,data.shape[0])
train = data[data['testing']==0]
test = data[data['testing']==1]
y_train = train['quality']
y_test = test['quality']
del train['quality']
del test['quality']
model = pyearth.Earth(max_degree = 2, max_terms = 100, penalty=3).fit(train,y_train)
y_test_hat = model.predict(test)
resid_test = y_test_hat - y_test
rsq_test = 1 - (numpy.std(resid_test)/numpy.std(y_test))**2
print model
print 'Testing RSQ:', rsq_test