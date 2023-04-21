import csv
import numpy as np
import math
import pandas as pd
df = pd.read_csv('./book1.csv')
# print(df)
import matplotlib.pyplot as plt
df_train = df[0:14]
df_test = df[14:]
z = df['T Shirt Size']
for i in len(z[0]):
    if z[i] == 'M':
        z[i] = 0
    else: 
        z[i] = 1
print(z)
x_train = df_train['Weight']
y_train = df_train['Height']
x_test = df_test['Weight']
y_test = df_test['Height']
plt.plot(x_train,y_train,"go",x_test, y_test, "r^")
plt.title('BMI')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.show()
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(x_train,y_train)


KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, p=2,
           weights='uniform')