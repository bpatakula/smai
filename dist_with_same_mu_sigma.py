# Author: Balaji Patakula
from matplotlib import pyplot as plt
import numpy as np
import math

# mean = 1/2, variance = 1/3

# uniform distribution function U[0,2], f(x) = 1/(b-a) for all values between a & b, otherwise 0
def create_uniform_dist():
    def f(x):
        if x > 0 and x <= 2:
            return 0.5
        else:
            return 0
    return f
f = create_uniform_dist()
x1 = list(range(-2,6,1))
y1 = list(map(f, x1))
line, = plt.plot(x1, y1, color='green', label='uniform density')

# random distribution function
s = np.random.normal(1/2, math.sqrt(1/3), 10000)
print("mean =" + str(np.mean(s)))
print("variance = " + str(np.std(s)**2))
count, bins = np.histogram(s, 100)
ndis_f = 1/(math.sqrt(1/3) * np.sqrt(2 * np.pi)) * np.exp( - (bins - 0.5)**2 / (2 * math.sqrt(1/3)**2))
plt.plot(bins, ndis_f,color='r',label='normal density')

plt.legend(loc='upper right')
line.set_drawstyle("steps")
plt.xlabel("x")
plt.ylabel("p(x)")
plt.show()
