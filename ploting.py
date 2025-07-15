import matplotlib.pyplot as plt
import numpy as np

# draw a line in a diagram
xpoints = np.array([-11,8])
ypoints = np.array([5,10])

plt.plot(xpoints, ypoints)
plt.show()

 # plotting without line
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

# plotting multiple points
xpoin = np.array([1,2,6,8])
ypoin = np.array([3,8,1,10])

plt.plot(xpoin, ypoin)
plt.show()

# plotting without x-points:

ypoints = np.array([3,8,1,10,5,7])

plt.plot(ypoints)
plt.show()

#matplotlib markers

mpoint = np.array([3,8,1,10,5,12])

plt.plot(mpoint, marker='H')  # there are so many marker read them from w3 school
plt.show()

# formating string fmt: we can also use the shortcut string notation parameter to specify the marker

ypints  = np.array([3,8,1,10,5,12])
plt.plot(ypints,'H--r') # there are so many option for color and make and which type line I want
plt.show()

# use marker size and color

ypoints = np.array([3,8,1,10,5,12])

plt.plot(ypoints,'o-.m',ms = 49,mfc='r',mec='b')
plt.show()

