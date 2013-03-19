'''
Created on Mar 13, 2013

@author: jasonrudy
'''
'''
    1. CRIM      per capita crime rate by town
    2. ZN        proportion of residential land zoned for lots over 
                 25,000 sq.ft.
    3. INDUS     proportion of non-retail business acres per town
    4. CHAS      Charles River dummy variable (= 1 if tract bounds 
                 river; 0 otherwise)
    5. NOX       nitric oxides concentration (parts per 10 million)
    6. RM        average number of rooms per dwelling
    7. AGE       proportion of owner-occupied units built prior to 1940
    8. DIS       weighted distances to five Boston employment centres
    9. RAD       index of accessibility to radial highways
    10. TAX      full-value property-tax rate per $10,000
    11. PTRATIO  pupil-teacher ratio by town
    12. B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks 
                 by town
    13. LSTAT    % lower status of the population
    14. MEDV     Median value of owner-occupied homes in $1000's
'''
import pandas
import pyearth
import patsy
import numpy
numpy.random.seed(0)

data = pandas.read_csv('housing.csv')
data['testing'] = numpy.random.binomial(1,0.2,data.shape[0])
train = data[data['testing']==0]
test = data[data['testing']==1]

model = pyearth.Earth(max_degree = 2, max_terms = 100, penalty=3).fit(patsy.dmatrices('MEDV ~ CRIM + ZN + INDUS + CHAS + NOX + RM + AGE + DIS + RAD + TAX + PTRATIO + B + LSTAT',data=train))
y_test_hat = model.predict(patsy.dmatrix('CRIM + ZN + INDUS + CHAS + NOX + RM + AGE + DIS + RAD + TAX + PTRATIO + B + LSTAT',data=test))
y_test = test['MEDV']
resid_test = y_test_hat - y_test
rsq_test = 1 - (numpy.std(resid_test)/numpy.std(y_test))**2
print model
print 'Testing RSQ:', rsq_test

