import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
import scipy.stats as scs
import seaborn as sns

# 1
print('-----1-----')
elements = (1, 2, 3, 4, 5, 6)
probabilities = (1/6, 1/6, 1/6, 1/6, 1/6, 1/6)
data = scs.rv_discrete(values=(elements, probabilities))
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Variance: ', data.var())
print('Standard deviation: ', data.std())
print('Expected value: ', data.expect())
print('Entropy: ', data.entropy())

# 2
print('-----2-----')
p = 0.2
n = 5
bernoulli = scs.bernoulli.rvs(p, size=100)
binomial = scs.binom.rvs(n, p, size=100)
poisson = scs.poisson.rvs(p, size=100)

# 3
print('-----3-----')
bernoulli_mean = bernoulli.mean()
bernoulli_var = bernoulli.var()
bernoulli_kur = scs.kurtosis(bernoulli)
bernoulli_skew = scs.skew(bernoulli)

binomial_mean = binomial.mean()
binomial_var = binomial.var()
binomial_kur = scs.kurtosis(binomial)
binomial_skew = scs.skew(binomial)

poisson_mean = poisson.mean()
poisson_var = poisson.var()
poisson_kur = scs.kurtosis(poisson)
poisson_skew = scs.skew(poisson)

print('Bernoulli')
print('Mean: ', bernoulli_mean)
print('Variance: ', bernoulli_var)
print('Kurtosis: ', bernoulli_skew)
print('Skewness: ', bernoulli_kur)

print('Binomial')
print('Mean: ', binomial_mean)
print('Variance: ', binomial_var)
print('Kurtosis: ', binomial_kur)
print('Skewness: ', binomial_skew)

print('Poisson')
print('Mean: ', poisson_mean)
print('Variance: ', poisson_var)
print('Kurtosis: ', poisson_kur)
print('Skewness: ', poisson_skew)

# 4
print('-----4-----')
plot = sns.distplot(bernoulli)
plot.set(xlabel='Bernoulli distribution', ylabel='Frequency')
plt.show()

plot = sns.distplot(binomial)
plot.set(xlabel='Binomial distribution', ylabel='Frequency')
plt.show()

plot = sns.distplot(poisson)
plot.set(xlabel='Poisson distribution', ylabel='Frequency')
plt.show()

# 5
print('-----5-----')
binomial = scs.binom.rvs(n=20, p=0.4, size=1000)
plot = sns.distplot(binomial)
plot.set(xlabel='Binomial distribution', ylabel='Frequency')
plt.show()
print("Probability sum: ", scs.binom.cdf(k=20, n=20, p=0.4))

# 6
print('-----6-----')
norm = scs.norm.rvs(size = 10000, loc=0, scale=2)
print('Mean: expected 0, actual ', norm.mean())
print('Variance: expected 4, actual ', norm.var())
print('Standard deviation: expected 2, actual ', norm.std())
print('Median: expected 0, actual ', scs.norm.median(loc=0, scale=2))
print('Expected value: expected 0, actual ', scs.norm.expect(loc=0, scale=2))
print('Kurtosis: expected 0, actual ', scs.kurtosis(norm))
print('Skewness: expected 0, actual ', scs.skew(norm))

# 7
print('-----7-----')
data1 = scs.norm.rvs(size=1000, loc=1, scale=2)
data2 = scs.norm.rvs(size=1000, loc=0, scale=1)
data3 = scs.norm.rvs(size=1000, loc=-1, scale=0.5)

plot = sns.distplot(data1, color='red')
plot = sns.distplot(data2, color='blue')
plot = sns.distplot(data3, color='black')

plt.show()