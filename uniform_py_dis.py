# Used to describe probability where every event has equal chances of occurring

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x=random.uniform(size=(2,3))
print(x)
# Visualization of Uniform Distribution
sns.displot(random.uniform(size=1000), kind="kde")
plt.show()

# Logistic distribution is used to describe growth. loc-mean, scale-standard deviation, size-the shape
x=random.logistic(1,2,(2,3))
print(x)
# visualization of logistic
sns.displot(random.logistic(size=(500)), kind="kde")
plt.show()

# difference between logistic and uniform
data = {
  "normal": random.normal(scale=2, size=1000),
  "logistic": random.logistic(size=1000)
}
sns.displot(data, kind="kde")
plt.show()