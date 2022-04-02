import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

training_data = pd.read_csv('iris.data')

training_data.columns = (
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width',
    'class'
)

feature_cols = [
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width'
]

label_cols = [
    'class'
]

values = training_data.loc[:, feature_cols]
labels = training_data.loc[:, label_cols].values.ravel()

values_train, values_test, labels_train, labels_test = train_test_split(values, labels, test_size=0.33)

logreg = LogisticRegression(solver='liblinear', multi_class='ovr')
clf=logreg.fit(values_train, labels_train)

print('Score: ', clf.score(values_test, labels_test))

pickle.dump(clf, open('./our_model.pkl', 'wb'))