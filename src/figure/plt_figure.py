'''
Created on 2017-07-19

@author: jack
'''

import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data

fig1 = plt.figure()

fig2 = plt.figure()

fig3 = plt.figure()

fig1.suptitle('sup title', fontsize=22)

ax1 = fig1.add_subplot(331)
ax1.plot(data[:,0], c='r')
ax1.plot(data[:,1], c='#ff00ff')

bx2 = fig2.add_subplot(332)
bx2.plot(data[0:,1], c='g')

# multiply relationship
fig3.suptitle('different size plots', fontsize=15)
cx1 = fig3.add_subplot(2,1,1)
cx2 = fig3.add_subplot(2,2,3)
cx3 = fig3.add_subplot(2,2,4)

cx1.plot(data[:,1])
cx3.plot(data[:,1])

plt.show()