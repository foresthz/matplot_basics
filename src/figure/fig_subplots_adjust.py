#encoding=utf-8
'''
Created on 2017-07-25

@author: jack
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data

fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()

# bottom=0.05, top=0.1
# space between horizontal space
fig1.subplots_adjust(hspace=1.5)

fig2.subplots_adjust(hspace=0.8)

fig3.subplots_adjust(hspace=0.3)

ax1 = fig1.add_subplot(221)
ax1.plot(data[:,0], c='r', marker='.')
ax1.set_xlabel('xxx1')
ax1.set_ylabel(u'长度0')

ax3 = fig1.add_subplot(223)
ax3.plot(data[:,1], c='b', marker='+')
ax3.plot(data[:,2], c='r', marker='.')

################################

bx1 = fig2.add_subplot(221)
bx1.plot(data[:,1], c='y', marker='*')
bx1.set_title(u'第二张图A')

bx3 = fig2.add_subplot(223)
bx3.plot(data[:,2], c='r', marker='+')
bx3.set_title(u'第二张图C')

#################################

cx1 = fig3.add_subplot(221)
cx1.plot(data[:,2], c='#110011', marker='+')
cx1.set_title(u'你好')

cx3 = fig3.add_subplot(223)
cx3.plot(data[:,3], c='#ff00ff', marker='.')
cx3.set_title(u'第三张图C')

plt.show()
