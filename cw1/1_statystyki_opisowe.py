import statistics as st
import numpy as np
import pandas as pd
from scipy import stats as sc
import matplotlib.pyplot as plt

# df = np.loadtxt("Wzrost.csv", delimiter=',', skiprows=0)
# print(df)
# print("Maksymalny wzrost - funkcja numpy:", np.max(df))
# print("Maksymalny wzrost:", df.max())
# print("Mediana wzrostu:", np.median(df))

# numpy funkcje: median, mean, std, min, max

# print("Odchylenie standardowe:", st.stdev(df))
# print("Odchylenie standardowe 2:", st.pstdev(df))

# statistics funkcje: median_high(), median_low(), pstdev(). stdev(), pvariance(), variance(), mode()

# scipy.stats funkcje: kurtosis(), skewness(), describe()

# cwiczenie 1
print("Cwiczenie 1")
data = np.loadtxt("MDR_RR_TB_burden_estimates_2020-10-29.csv", delimiter=',', usecols=(10,), skiprows=1)
print("Maksimum:", data.max())
print("Minimum:", data.min())
print("Mediana:", np.median(data))
print("Mediana high:", st.median_high(data))
print("Mediana low:", st.median_low(data))
print("Średnia:", data.mean())
print("Odchylenie standardowe:", st.stdev(data))
print("Odchylenie standardowe 2:", st.pstdev(data))
print("Wariancja:", st.variance(data))
print("Wariancja 2:", st.pvariance(data))
print("Mode:", st.mode(data))

# cwiczenie 2
print()
print("Cwiczenie 2")
data2 = np.loadtxt("Wzrost.csv", delimiter=',', skiprows=0)

print("Mediana high:", st.median_high(data2))
print("Mediana low:", st.median_low(data2))
print("Odchylenie standardowe:", st.stdev(data2))
print("Odchylenie standardowe 2:", st.pstdev(data2))
print("Wariancja:", st.variance(data2))
print("Wariancja 2:", st.pvariance(data2))
print("Mode:", st.mode(data2))

# cwiczenie 3
print()
print("Cwiczenie 3")
print("Kurtosis:", sc.kurtosis(data2))
print(sc.describe(data2))
print("Skewness:", sc.skew(data2))
print("Powtórzenia:", sc.find_repeats(data2))
print("Entropy:", sc.entropy(data2))
print("Trimmed min:", sc.tmin(data2))
print("Trimmed max:", sc.tmax(data2))
print("Nth moment:", sc.moment(data2))
print("Bayesian confidence intervals  :", sc.bayes_mvs(data2))
# other scipy.stats functions trim_mean(), iqr(), sem(), gstd(), mvdist(),
# https://docs.scipy.org/doc/scipy/reference/stats.html

# cwiczenie 4
columns = ["Gender", "FSIQ", "VIQ", "PIQ", "Weight", "Height", "MRI_Count"]
df = pd.read_csv("brain_size.csv", sep=";", usecols=columns)
print(df.head())
print("Średnia VIQ: ", df["VIQ"].mean())
print("Liczba kobiet: ", df[df.Gender == "Female"].shape[0])
print("Liczba mężczyzn: ", df[df.Gender == "Male"].shape[0])
plt.hist(df.VIQ)
plt.title("VIQ")
plt.show()
plt.hist(df.PIQ)
plt.title("PIQ")
plt.show()
plt.hist(df.FSIQ)
plt.title("FSIQ")
plt.show()

plt.hist(df[df.Gender == "Female"].VIQ)
plt.title("VIQ kobiety")
plt.show()
plt.hist(df[df.Gender == "Female"].PIQ)
plt.title("PIQ kobiety")
plt.show()
plt.hist(df[df.Gender == "Female"].FSIQ)
plt.title("FSIQ kobiety")
plt.show()
