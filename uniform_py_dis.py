# Used to describe probability where every event has equal chances of occurring

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x=random.uniform(size=(2,3))
print(x)
sns.displot(random.uniform(size=1000),kind="kde")
plt.show()