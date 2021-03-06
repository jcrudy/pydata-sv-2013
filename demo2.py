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
y = 2 + (x-1)*(x<1)*-1 + 3*(x-1)*(x>1)*(4-x)*(x<4) + .1*(x-1)*(x>1)

pyplot.figure(figsize=(10,5))
pyplot.plot(x,y)
ax = pyplot.gca()
XKCDify(ax)
pyplot.setp(ax, frame_on=False)
pyplot.savefig('demo2.pdf',transparent=True)




