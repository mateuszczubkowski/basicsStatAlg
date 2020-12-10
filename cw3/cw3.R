library(Rlab)
# 1
probabilities <- rep(1/6, 6)
elements <- seq(1, 6, 1)

elmean = mean(elements)
elmedian = median(elements)
elstd = sd(elements)
elvar = var(elements)

# 2
n = 100
p = 0.2
k = 5

ber <- rbern(n,p)
bin <- rbinom(n,k,p)
poi <- rpois(n,p)

# 3
mean(ber)
median(ber)
var(ber)
skew(ber)
kurt(ber)

mean(bin)
median(bin)
var(bin)
skew(bin)
kurt(bin)

mean(poi)
median(poi)
var(poi)
skew(poi)
kurt(poi)

# 4
hist(bin)

hist(poi)

# 5
poi <- rpois(20,0.4)
P <- ecdf(poi)
plot(P)

bin <- rbinom(20,20,0.4)
P <- ecdf(bin)
plot(P)

# 6
norm <- rnorm(10, 0, 2)

print('mean - 0')
mean(norm)
print('median - 0')
median(norm)
print('variance - 4')
var(norm)
print('skewness - 0')
skew(norm)
print('kurtosis - 0')
kurt(norm)

norm <- rnorm(100, 0, 2)

print('mean - 0')
mean(norm)
print('median - 0')
median(norm)
print('variance - 4')
var(norm)
print('skewness - 0')
skew(norm)
print('kurtosis - 0')
kurt(norm)

norm <- rnorm(1000, 0, 2)

print('mean - 0')
mean(norm)
print('median - 0')
median(norm)
print('variance - 4')
var(norm)
print('skewness - 0')
skew(norm)
print('kurtosis - 0')
kurt(norm)

norm <- rnorm(10000, 0, 2)

print('mean - 0')
mean(norm)
print('median - 0')
median(norm)
print('variance - 4')
var(norm)
print('skewness - 0')
skew(norm)
print('kurtosis - 0')
kurt(norm)

# 7
norm1 <- rnorm(1000, 1, 2)
norm2 <- rnorm(1000, 0, 1)
norm3 <- rnorm(1000, -1, 0.5)

hist(norm1)
hist(norm2)
hist(norm3)