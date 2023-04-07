# Import necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Write "%matplotlib inline" for jupyter
import seaborn as sns
import csv
import warnings
warnings.filterwarnings('ignore')

#Import train dataset

df = pd.read_csv('train.csv')

# print(df.head())  
# print(df.shape)
# print(df.dtypes)

# Dropping unwanted columns

df = df.drop('Name', axis=1)
df = df.drop('Ticket', axis=1)
df = df.drop('Fare', axis=1)
df = df.drop('Cabin', axis=1)

# Let us combine number of sibling/spouse and number of parents/children

df['Family'] = df['SibSp'] + df['Parch'] + 1
# Drop used features no longer required

df = df.drop('SibSp', axis=1)
df = df.drop('Parch', axis=1)

# print (df.describe())
# count in Age is 714 so there are NaNs

df['Age'] = df['Age'].fillna(df['Age'].median())
# print (df.describe())



