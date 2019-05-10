from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
import pandas as pd
data = pd.read_csv("FCFB.csv")
X = data.drop('Class', axis = 1)
y = data.Class
param_grid = {'logisticregression__C': [0.001, 0.01, 0.1, 1, 10, 100]}
pipe = make_pipeline(StandardScaler(), LogisticRegression(penalty = 'l2'))
grid = GridSearchCV(pipe, param_grid, cv = 10)
grid.fit(X, y)
print(grid.best_params_)
X_scaled = StandardScaler().fit_transform(X)
clf = LogisticRegression(penalty = 'l2', C = 1)
clf.fit(X_scaled,y)
abs_feat = []
num_features = len(X.columns)
for i in range(num_features):
    coef = clf.coef_[0, i]
    abs_feat.append((abs(coef), X.columns[i]))
l = []
sum = avg = 0
for i in sorted(abs_feat,reverse=True):
    print(i[0],i[1])
    l.append(i[0])
print(l)
for i in l:
    sum = sum+i
avg = sum/len(l)
print(avg)
import numpy as np
print(np.median(l))
