import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
# from sklearn.impute import SimpleImputer


dataset = pd.read_csv('E:/100-Days-Of-ML-Code/datasets/Data.csv')
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , 3].values

#imputer = SimpleImputer(missing_values = "NaN", strategy = "mean")
imputer = Imputer(missing_values = "NaN", strategy = "median", axis = 0)
imputer = imputer.fit(X[ : , 1:3])
X[ : , 1:3] = imputer.transform(X[ : , 1:3])

labelencoder_X = LabelEncoder()
X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])

# onehotencoder = OneHotEncoder(categorical_features = [0])
# X = onehotencoder.fit_transform(X).toarray()
# labelencoder_Y = LabelEncoder()
# Y =  labelencoder_Y.fit_transform(Y)

X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size = 0.2, random_state = 0)
print(X)
print(Y)

print(X_train)
print(X_test)

print(Y_train)
print(Y_test)
