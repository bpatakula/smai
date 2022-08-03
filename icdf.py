from matplotlib import pyplot as plt
import random 
import math
import numpy as np
from scipy import stats

def random_inverse_cdf(p, mean, std):
    return stats.norm.ppf(p,loc=mean,scale=std)

def random_pdf(x, mean, std):
    return stats.norm.pdf(x,loc=mean,scale=std)

def rayleigh_inverse_cdf(p, std):
     return stats.rayleigh.ppf(p, scale=std)

def rayleigh_pdf(x, std):
    return stats.rayleigh.pdf(x, scale=std)
                       
def exponential_inverse_cdf(p, lambd):
    #return -(lambd)* np.log(1-p)
    return stats.expon.ppf(p, loc=lambd)

def exponential_pdf(x, lambd):
    #return (1/lambd)* np.exp(-x/lambd)
    return stats.expon.pdf(x, loc=lambd)


u = np.random.random(10000)


plt.subplot(121)
#mu = 1.5
v = exponential_inverse_cdf(u,1.5)
data, bin_values = np.histogram(v, 100)
pdf, bins, patches = plt.hist(v, 100, density=True)
plt.title('Exponential Random Variables')


plt.subplot(122)
plt.plot(bin_values, exponential_pdf(bin_values,1.5))
plt.title('Exponential PDF')
plt.show()

plt.subplot(221)
v = random_inverse_cdf(u,0,3)
data, bin_values = np.histogram(v, 100)
pdf, bins, patches = plt.hist(v, 100, density=True)
plt.title('Normal Random Variables')

plt.subplot(222)
plt.plot(bin_values, random_pdf(bin_values,0,3))
plt.title('Normal PDF')
plt.show()


plt.subplot(321)
v = rayleigh_inverse_cdf(u, 1)
data, bin_values = np.histogram(v, 100)
pdf, bins, patches = plt.hist(v, 100, density=True)
plt.title('Rayleigh Random Variables')

plt.subplot(322)
plt.plot(bin_values, rayleigh_pdf(bin_values,1))
plt.title('Rayleigh PDF')
plt.show()
