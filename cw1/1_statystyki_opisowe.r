# 1
setwd("C:/Users/PatMat/Desktop/STUDIA/basicsStatAlg/cw1")
data = read.csv("napoje_po_reklamie.csv", row.names = 1, header = TRUE,sep=";")
typeof(data) # list
sapply(data, mean) 
sapply(data, sd) 
sapply(data, var) 
sapply(data, min) 
sapply(data, max) 
sapply(data, median) 
sapply(data, range) 
sapply(data, quantile)
# 2
pepsi = as.numeric(unlist(data["pepsi"]))
fanta = as.numeric(unlist(data["fanta"]))
mean(pepsi)
sd(pepsi)
var(pepsi)
min(pepsi)
max(pepsi)
median(pepsi)
range(pepsi)
mean(fanta)
sd(fanta)
var(fanta)
min(fanta)
max(fanta)
median(fanta)
range(fanta)
# 3
data1 = as.numeric(unlist(read.csv("Wzrost.csv", header = FALSE,sep=",")))
mean(data1)
sd(data1)
var(data1)
min(data1)
max(data1)
median(data1)
range(data1)