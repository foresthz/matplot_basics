'''
Created on 2017-06-28

@author: jack
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(5,15,0.2)
y = np.sin(x)

# lot's of options should be used
plt.plot(x,y, marker='+')
plt.title('plot sin curve')

plt.show()