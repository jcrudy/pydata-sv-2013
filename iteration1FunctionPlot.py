'''
Created on Mar 7, 2013

@author: jasonrudy
'''
import numpy
from matplotlib import pyplot
from xkcdify import XKCDify
x = numpy.arange(-10,10,.1)
y = abs(x)

fig = pyplot.figure()
pyplot.plot(x,y)
ax = pyplot.gca()
ax.set_xlim(-10, 10)
ax.set_ylim(0,10)
XKCDify(ax)
pyplot.savefig('iteration1.pdf',transparent=True)