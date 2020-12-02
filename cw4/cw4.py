import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
import scipy.stats as scs
import seaborn as sns

# 1
print('-----1-----')
norm = scs.norm.rvs(size=200, loc=2, scale=30)
print(norm.mean())

test_sredniej = scs.ttest_1samp(norm, 2.5)
print(test_sredniej)

# 2
print('-----2-----')
data = pd.read_csv('napoje.csv', delimiter=";")
test_lech = scs.ttest_1samp(data['lech'], 60500)
print("lech")
print(data["lech"].mean())
print(test_lech)

test_cola = scs.ttest_1samp(data['cola'], 222000)
print('cola')
print(data['cola'].mean())
print(test_cola)

test_regio = scs.ttest_1samp(data['regionalne'], 43500)
print('regionalne')
print(data['regionalne'].mean())
print(test_regio)

# 3
print('-----3-----')
columns = ['pepsi', 'fanta', 'zywiec', 'regionalne', 'cola', 'lech']

alpha = 0.2
print('Dla alpha = 0.2, test D’Agostino i Pearson')
for column in data.columns:
    p = scs.normaltest(data[column])[1]
    if(p < alpha):
        print('Zmienna ' + column + ' nie pochodzi z rozkładu normalnego, wartość p: ', p)
    else:
        print('Zmienna ' + column + ' pochodzi z rozkładu normalnego, wartość p: ', p)

# 4
print('-----4-----')
okocim_lech_nz = scs.ttest_ind(data['okocim'], data['lech'])
okocim_lech_z = scs.ttest_rel(data['okocim'], data['lech'])
fanta_regionalne_nz = scs.ttest_ind(data['fanta '], data['regionalne'])
fanta_regionalne_z = scs.ttest_rel(data['fanta '], data['regionalne'])
cola_pepsi_nz = scs.ttest_ind(data['cola'], data['pepsi'])
cola_pepsi_z = scs.ttest_rel(data['cola'], data['pepsi'])

print('Statystyka T i prawdopodobienstwo dla średnich okocim-lech niezależne: ', okocim_lech_nz)
print('Statystyka T i prawdopodobienstwo dla średnich okocim-lech zależne: ', okocim_lech_z)
print('Statystyka T i prawdopodobienstwo dla średnich fanta-regionalne niezależne: ', fanta_regionalne_nz)
print('Statystyka T i prawdopodobienstwo dla średnich fanta-regionalne zależne: ', fanta_regionalne_z)
print('Statystyka T i prawdopodobienstwo dla średnich cola-pepsi niezależne: ', cola_pepsi_nz)
print('Statystyka T i prawdopodobienstwo dla średnich cola-pepsi zależne: ', cola_pepsi_z)
