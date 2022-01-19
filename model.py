import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle

X = pd.read_csv('CR_Train.csv')
Y = pd.read_csv('CR_Test.csv')

Y = Y.values.reshape(119209,)

# Training using Train-Test Split

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(X,Y, test_size=0.2, random_state=20)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

log_reg=LogisticRegression()
svc_model=SVC()
log_reg=log_reg.fit(x_train, y_train)
svc_model=svc_model.fit(x_train, y_train)
print(log_reg.score(x_test, y_test))

pickle.dump(log_reg, open('log_reg.pkl','wb'))