'''
Created on Mar 7, 2013

@author: jasonrudy
'''
import numpy
from matplotlib import pyplot
from xkcdify import XKCDify
x = numpy.arange(-10,10,.1)
y = x ** 0

fig = pyplot.figure()
pyplot.plot(x,y)
ax = pyplot.gca()
ax.set_xlim(-10, 10)
ax.set_ylim(0,2)
XKCDify(ax)
pyplot.savefig('iteration0.pdf',transparent=True)