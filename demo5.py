'''
Created on Mar 7, 2013

@author: jasonrudy
'''
import numpy
from pyearth import Earth
from matplotlib import pyplot
from xkcdify import XKCDify
'''
(Intercept)                   No      8.36475      
h(x6-1.13136)                 No      -6.86652     
h(1.13136-x6)                 No      15.4224      
h(x6+8.56802)*h(1.13136-x6)   No      -1.00847     
h(-8.56802-x6)*h(1.13136-x6)  No      1.00063      
x6*h(x6-1.13136)              No      0.999736  
'''
m = 1000
x = numpy.arange(-10,10,.1)
y = (x-1)*(x>1)*(x-1)*(x>1) + (1-x)*(x<1)*(1-x)*(x<1)
#y = 8 - 6*(x-1)*(x>1) + 15*(1-x)*(x<1) - 1*(x+8)*(x>-8)*(1-x)*(x<1) + 1*(-8-x)*(x<-8)*(1-x)*(x<1) + x*(x-1)*(x>1)

pyplot.figure(figsize=(10,5))
pyplot.plot(x,y)
ax = pyplot.gca()
XKCDify(ax)
pyplot.savefig('demo4.pdf',transparent=True)




