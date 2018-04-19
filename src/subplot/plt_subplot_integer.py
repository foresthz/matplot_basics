'''
Created on 2017-06-29

@author: jack
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import random

# this title not works
plt.title('plot 8 figures')

plt.subplot(331)

x1=[1,5,12,-3,-13,6]
plt.plot(x1, marker='+')

plt.subplot(332)
x2=[3,5,11,2,-3,8]
plt.plot(x2, marker='*')

plt.subplot(333)
x3=np.arange(2,10,0.5)
y3=np.sin(x3)
plt.plot(x3,y3,marker='o')

plt.subplot(334)
x4=random(10)
y4=np.cos(x4)
plt.plot(x4,y4,marker='x', linestyle='None')

plt.subplot(335)
x5=np.linspace(1,100,12)
y5=np.log2(x5)
plt.plot(x5,y5,marker='^', linestyle='-.')

plt.subplot(336)
x6=random(10)
y6=np.cos(x6)
# if linestyle is None, and marker is not setup, then nothing will be drawn
plt.plot(x6,y6,color='red', linestyle='None', marker='*')

axes7 = plt.subplot(337)
x7=np.linspace(-10,10,30)
y7=x7*x7
plt.plot(x7,y7,color='y', marker='.')


# subplot is not forced to be invoked by order
plt.subplot(339)
x9=np.linspace(-10,10,24)
y9=np.tan(x9)
# css style color is supported by matplotlib
plt.plot(x9,y9,color='#00ff00', marker='+')


plt.show()