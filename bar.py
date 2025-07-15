import matplotlib.pyplot as plt
import numpy as np

x=np.array(['A','B','C','D','E'])
y=np.array([5,2,6,3,9])
plt.bar(x,y,color='r',width=0.5)
plt.show()