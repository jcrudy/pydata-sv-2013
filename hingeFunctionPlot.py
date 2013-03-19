'''
Created on Mar 7, 2013

@author: jasonrudy
'''
import numpy
from matplotlib import pyplot
from xkcdify import XKCDify
x = numpy.arange(-10,10,.1)
y = x * (x > 0)

fig = pyplot.figure(figsize=(10,5))
pyplot.plot(x,y)
ax = pyplot.gca()
XKCDify(ax)
pyplot.show()
pyplot.savefig('hinge.pdf',transparent=True)