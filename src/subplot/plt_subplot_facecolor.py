'''
Created on 2017-07-04

@author: jack
'''
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(339)
x9=np.linspace(-20,20,30)
y9=x9*x9+np.power(x9,3)
# number stands for some grey color, more bright if the number is larger
plt.plot(x9,y9,marker='.', c='0.75')

plt.subplot(331)
x1=np.arange(-20,20,1)
y1=np.power(x1,4)+np.power(x1,3)
plt.plot(x1,y1,marker='.', c='0.3')

plt.subplot(332)
x2=np.arange(-5,5,0.2)
y2=np.sin(x2)+np.power(np.cos(x2),2)
plt.plot(x2,y2,marker='*', c='#33ff33')


plt.subplot(333)
x3=np.arange(-10,10,1)
y3=np.sin(np.cos(x3) + np.power(np.sin(x3),3))
# ls stands for linestyle
plt.plot(x3,y3,marker='.', c='r', ls='None')

# cycle anallysis, as a overview
plt.subplot(334)
x4=np.arange(-8,8,0.2)
y4=np.sin(x4)+np.cos(x4)
plt.plot(x4,y4,marker='+', c='g')
# could plot two lines
plt.plot(x2,y2,c='r')

plt.subplot(335)
x5=np.arange(-30,30,0.5)
y5=np.power(x5,2)*3*np.sin(x5)+np.cos(x5*x5)*x5*5
# [0,1] darker --> lighter
plt.plot(x5,y5,marker='.',c='0.95')


plt.show()