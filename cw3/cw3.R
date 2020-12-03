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