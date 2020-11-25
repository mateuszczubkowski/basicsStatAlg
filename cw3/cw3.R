elements = c(1, 2, 3, 4, 5, 6)
probabilities = c(1/6, 1/6, 1/6, 1/6, 1/6, 1/6)
data = rvdiscrete(n = 1, elements, probabilities)

sapply(data, mean) 