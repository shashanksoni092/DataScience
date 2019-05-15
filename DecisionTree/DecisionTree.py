#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 00:31:24 2018

@author: shashanksoni092
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iris=datasets.load_iris()
iris #Dictionary
iris_data=iris["data"]# changing into ndarray from dictionary element


type(iris_data)

iris_data=pd.DataFrame(iris_data) #converting into dataframe but still column name is not there


iris_data.columns

iris_data.rename(columns={0:'sepal_length',1:'sepal_width',2:'petal_length',3:'petal_width'},inplace=True)

iris_data.columns

target=iris['target']
target=pd.DataFrame(target)
target.columns
target.head


target.rename(columns={0:'species'},inplace=True)

target.columns
target.head

#unique values of species
target['species'].unique()

target['species'].value_counts()

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


x_train1,x_test1,y_train1,y_test1=train_test_split(iris_data,target,test_size=0.2)

model=DecisionTreeClassifier(criterion='entropy')

model.fit(x_train1,y_train1)

preds=model.predict(x_test1)

preds

pd.Series(preds).value_counts()

preds_df=pd.DataFrame(preds)

#Caculating accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_test1,preds)
#Accuracy 81.25

from sklearn.tree 
from IPython.display import SVG
from graphviz import Source
import DecisionTreeClassifier, export_graphviz
from IPython.display import display
from sklearn import tree

export_graphviz(model,out_file='tree.dot')

!dot -Tpng tree_limited.dot -o tree_limited.png -Gdpi=600

from IPython.display import Image
Image(filename = 'tree_limited.png')


from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])


sudo pip install pydot

