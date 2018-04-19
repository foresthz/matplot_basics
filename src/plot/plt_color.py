'''
Created on 2017-07-06

@author: jack
'''
import matplotlib.pyplot as plt
from sklearn import datasets
iris=datasets.load_iris()
data = iris.data
target = iris.target

plt.subplot(332, facecolor='#f0f0f0')
x1 = data[:,0]
x2 = data[:,1]
x3 = data[:,2]
x4 = data[:,3]
plt.plot(x2, marker='+', linestyle='None', c='g')
plt.plot(x1, marker='+', linestyle='None', c='r')

plt.subplot(335, facecolor='y')
plt.plot(x2,marker='.', c='b')

plt.subplot(339, facecolor='#111111')
plt.plot(x1, c='r')
plt.plot(x2, c='g')
plt.plot(x3, c='b')
plt.plot(x4, c='y')

plt.subplot(331, facecolor='#72af93')
plt.plot(x1, c='r')
plt.plot(x2, c='b')


plt.show()