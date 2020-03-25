#Exercise 3: Speed and Gas Mileage

import pandas as pd
import csv
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import math

df = pd.read_csv("Pearson_Prob_3.csv",
                    dtype={'Miles/Hour_x': float , 'Miles/Gallon_y': float})

X = df['Miles/Hour_x']
Y = df['Miles/Gallon_y']

plt.scatter(X, Y)
plt.xlabel("Miles/Hour_x")
plt.ylabel("Miles/Gallon_y")
plt.title('Exercise 3: Speed and Gas Mileage')
plt.gcf().autofmt_xdate()
plt.savefig("Exercise_3.png")
plt.show()

#Pearson FUnction implementation using  Manually
Xmean = sum(X)/len(X)
Ymean = sum(Y)/len(Y)

x = [var-Xmean for var in X]
y = [var-Ymean for var in Y]

xy =[a*b for a,b in list(zip(x,y))]
sum_xy = sum(xy)

x_square = [a*a for a in x]
y_square = [b*b for b in y]

sum_x_square = sum(x_square)
sum_y_square = sum(y_square)

sum_x_square_sum_y_square = sum_x_square*sum_y_square
sqrt_sum_x_square_sum_y_square = math.sqrt(sum_x_square_sum_y_square)

r = sum_xy/sqrt_sum_x_square_sum_y_square
print('Pearsons correlation calcuation using Manually: %.4f' % r)

#Pearson Implementation using python library
pearsoncorr, _ = pearsonr(X,Y)
print('Pearsons correlation calcuation using Python Library: %.4f' % pearsoncorr)