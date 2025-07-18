import multiprocessing as mp
import time
import numpy as np

print(f"Number of CPUs: {mp.cpu_count()}")

# Serial version
def random_square(seed):
    np.random.seed(seed)
    random_num=np.random.randint(0,10)
    return random_num

t0=time.time()
results=[]
for i in range(1000000):
    results.append(random_square(i))
t1=time.time()
print(f'Serial Execution time: {t1-t0}')


# parallel version
t0=time.time()
n_cpu=mp.cpu_count()

pool=mp.Pool(processes=n_cpu)
results = pool.map(random_square, range(1000000))
t1=time.time()
print(f'Parallel CPU Execution time: {t1-t0}')

