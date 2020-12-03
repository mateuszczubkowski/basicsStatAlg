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

# 5
print('-----5-----')
okocim_lech_var = scs.levene(data['okocim'], data['lech'])
fanta_regionalne_var = scs.levene(data['fanta '], data['regionalne'])
regionalne_cola_var = scs.levene(data['regionalne'], data['cola'])

print('Statystyka T i prawdopodobienstwo dla wariancji okocim-lech: ', okocim_lech_var)
print('Statystyka T i prawdopodobienstwo dla wariancji fanta-regionalne: ', fanta_regionalne_var)
print('Statystyka T i prawdopodobienstwo dla wariancji regionalne-cola: ', regionalne_cola_var)

# 6
print('-----6-----')
regionalne_2001_2015 = scs.ttest_rel(data.loc[data['rok'] == 2001]['regionalne'], data.loc[data['rok'] == 2015]['regionalne'])
print(regionalne_2001_2015)

# 7
print('-----7-----')
data1 = pd.read_csv('napoje_po_reklamie.csv', delimiter=";")
cola = scs.ttest_rel(data.loc[data['rok'] == 2016]['cola'], data1['cola'])
fanta = scs.ttest_rel(data.loc[data['rok'] == 2016]['fanta '], data1['fanta '])
pepsi = scs.ttest_rel(data.loc[data['rok'] == 2016]['pepsi'], data1['pepsi'])

print(cola)
print(fanta)
print(pepsi)
