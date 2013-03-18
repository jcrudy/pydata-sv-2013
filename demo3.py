'''
Created on Mar 7, 2013

@author: jasonrudy
'''
import numpy
from pyearth import Earth
from matplotlib import pyplot
from xkcdify import XKCDify
m = 1000
x = numpy.arange(-10,10,.1)
y = 1+2*(x-1)*(x<1) + 0.5*(x-1)*(x>1)

pyplot.figure(figsize=(10,5))
pyplot.plot(x,y)
ax = pyplot.gca()
XKCDify(ax)
pyplot.savefig('demo3.pdf',transparent=True)




