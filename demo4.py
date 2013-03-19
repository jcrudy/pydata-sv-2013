'''
Created on Mar 7, 2013

@author: jasonrudy
'''
import numpy
from pyearth import Earth
from matplotlib import pyplot
from xkcdify import XKCDify


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()



m = 1000
x = numpy.arange(-10,10,.1)
y = (x-1)*(x>1)*(x-1)*(x>1) + (1-x)*(x<1)*(1-x)*(x<1)
#y = 8 - 6*(x-1)*(x>1) + 15*(1-x)*(x<1) - 1*(x+8)*(x>-8)*(1-x)*(x<1) + 1*(-8-x)*(x<-8)*(1-x)*(x<1) + x*(x-1)*(x>1)

pyplot.figure(figsize=(10,5))
pyplot.plot(x,y)
ax = pyplot.gca()
XKCDify(ax)
pyplot.savefig('demo4.pdf',transparent=True)




