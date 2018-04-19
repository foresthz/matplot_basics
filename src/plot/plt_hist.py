'''
Created on 2017-07-17

@author: jack
'''

import matplotlib.pyplot as plt
from sklearn import datasets


iris = datasets.load_iris()
data = iris.data



ax2 = plt.subplot(332)
ax2.hist(data[:,0], color='#0000ff', bins=50)
ax2.set_title('bins=50')

ax3 = plt.subplot(333)

ax4 = plt.subplot(334)

ax3.hist(data[:,0], color='r', bins=5)
ax3.set_title('bins=5')

ax4.hist(data[:,0], color='g', bins=100)
ax4.set_title('bins=100')

print 'title of axes 3', ax3.get_title()

ax5 = plt.subplot(335)
ax5.set_title('555')

#plt.title('with different bins')

plt.show()
