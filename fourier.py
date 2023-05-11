# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
import sys

#%%
data = pd.read_excel('candy_production.xlsx')

#%%


def sampling(data,prev):
    n = len(data)
    i = np.random.randint(prev, n - 1)
    x = np.arange(i - prev, i)
    return [data[t] for t in x], data[i]

n = int(input())
traffic = []
for i in range(n):
    traffic.append(int(input()))
offset = 7
last = 130
X = []
for t in range(n - last, n):
    z = [t]
    z.extend([1 if w == t % offset else 0 for w in range(offset)])
    X.append(z)
Y = traffic[-last:]
res = sm.OLS(Y, X).fit()


X = []
for t in range(30):
    z = [n + t]
    z.extend([1 if w == (n + t) % offset else 0 for w in range(offset)])
    X.append(z)
ans = res.predict(X)

for x in ans: 
    print(x) 
