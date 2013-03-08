'''
Created on Mar 7, 2013

@author: jasonrudy
'''
import numpy
from pyearth import Earth
from matplotlib import pyplot
m = 1000
x = 20*(numpy.random.uniform(size=(m,1)) - .5)
y = x[:,0]*(x[:,0]<0)*-1 + x[:,0]*(x[:,0]>0)*2 + 10*numpy.random.normal(size=m)
print y.shape
print y.dtype
print y
print x.shape
print x.dtype

model = Earth()
model.fit(x,y)
y_hat = model.predict(x)
print model.trace()
print model
pyplot.figure(figsize=(10,5))
pyplot.plot(x[:,0],y,'r.')
pyplot.plot(x[:,0],y_hat,'b.')
ax = pyplot.gca()
pyplot.setp(ax, frame_on=False)
pyplot.savefig('demo.pdf',transparent=True)




