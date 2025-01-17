import numpy as np
from scipy import stats

age = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
fat_percent = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
age = np.array(age)
fat_percent = np.array(fat_percent)
data = np.vstack([age, fat_percent]).reshape([-1, ], order='F')
print( np.vstack([age, fat_percent]))
print(data)

print(stats.describe(data))
