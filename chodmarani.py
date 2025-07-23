import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

sns.displot([0, 1, 2, 3, 4, 5])       # displot in histogram
sns.displot([0, 1, 2, 3, 4, 5],kind='kde')   # plotting a displot without the histogram
plt.show()


# normal distribution
sns.displot(random.normal(size=1000),kind='kde')
plt.show()

# Binomial Distribution is a Discrete Distribution . It has three parameters
# n - number of trials.
# p - probability of occurrence of each trial (e.g. for toss of a coin 0.5 each).
# size - The shape of the returned array.

x=random.binomial(10,0.5,10)
print(x)
sns.displot(random.binomial(10,0.5,1000))
plt.show()

# Difference between normal and binomial
data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}
sns.displot(data, kind="kde")
plt.show()

