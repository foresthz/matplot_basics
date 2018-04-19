'''
Created on 2017-07-17

@author: jack
'''

import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data

ax4 = plt.subplot(334)

ax2 = plt.subplot(332)
ax2.plot(data[:,0], c='r')

plt.subplot(331)
# plot current axes
plt.plot(data[:,0], c='b')

# could point to specific axes anywhere
ax4.plot(data[:,0], c='g')
ax4.set_title(' 444 ')

plt.show()
