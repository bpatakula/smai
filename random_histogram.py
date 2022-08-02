import random
import matplotlib.pyplot as plt
import numpy as np

def RandomSum(size):
    x = 0
    for j in range(size):
        x = x + random.random()
    return x

def histogram_bins_range(data, desired_bin_size):
    min_val = np.min(data)
    max_val = np.max(data)
    n_bins = range(int(min_val), int(max_val) + 1 , desired_bin_size)
    return n_bins

sum_rand = [0] * 50000
for k in range(50000):
    sum_rand[k] = RandomSum(500)

plt.hist(sum_rand, edgecolor="red", bins=histogram_bins_range(sum_rand,1), density=True)
plt.show()
