import matplotlib.pyplot as plt
import numpy as np

# first plot
xpoints = np.array([-11,8])
ypoints = np.array([5,10])

plt.plot(xpoints, ypoints)
plt.show()

 # second plot
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

# third plot
xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])
plt.plot(xpoints, ypoints)
plt.show()