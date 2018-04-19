#coding=utf-8
'''
Created on 2017-07-19

@author: jack
'''

import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
data = iris.data

fig1 = plt.figure()

fig2 = plt.figure()

fig3 = plt.figure()

ax2 = fig1.add_subplot(332)
ax2.plot(data[:,0], c='r', marker='+')
ax2.set_xlabel(u'你好')

fig1.canvas.set_window_title(u'Picture  哦哦  1')

bx2 = fig2.add_subplot(222)
bx2.plot(data[:,0], c='g', marker='*')
bx2.plot(data[:,1], c='b', marker='+')
bx2.set_xlabel(u'x2 x2你好')

bx4 = fig2.add_subplot(224)

bx4.set_xlabel('x4 x4')
bx4.plot(data[:,1], c='b', marker='+')
x1 = np.linspace(1,20,30)
y1 = np.sin(x1)

cx2 = fig3.add_subplot(332)
cx2.plot(x1, y1, c='g', marker='^')


plt.show()