from matplotlib.pylab import logistic
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import cross_validate

df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn (1).csv')
print(df.size)
print(pd.DataFrame(df.dtypes).rename(columns = {0:'dtype'}))

fig = plt.figure(figsize=(10,6))
ax = fig.gca()
df.boxplot(column = 'MonthlyCharges', by = 'Churn', ax = ax)
ax.set_ylabel("MonthlyCharges")
plt.show()

fig = plt.figure(figsize=(10,6))
ax = fig.gca()
df.boxplot(column = 'tenure', by = 'Churn', ax = ax)
ax.set_ylabel("Tenure")
plt.show()

df['class'] = df['Churn'].apply(lambda x : 1 if x == "Yes" else 0)

X = df[['tenure','MonthlyCharges']].copy()
y = df['class'].copy()


X_train, X_test, y_train, y_test = train_test_split( X,y , test_size = 0.2, random_state = 0)
print(X_train)
print(X_test)

print(y_train.value_counts())

print(y_test.value_counts())

clf = LogisticRegression(fit_intercept=True, max_iter=10000)
clf.fit(X_train,y_train)

print(clf.coef_)
print(clf.intercept_)

train_preds = clf.predict_proba(X_train)
test_preds = clf.predict_proba(X_test)
print(train_preds)
print(test_preds)
print(X_test)


train_class_preds = clf.predict(X_train)
test_class_preds = clf.predict(X_test)
print(train_class_preds)
print(test_class_preds)

train_accurancy = accuracy_score(train_class_preds, y_train)
test_accurancy = accuracy_score(test_class_preds, y_test)
print(train_accurancy)
print(test_accurancy)

# labels = ['Retained', 'Churned']
# cm = confusion_matrix(y_train, train_class_preds)
# print(cm)
# ax= plt.subplot()
# sns.heatmap(cm, annot=True, ax = ax) 
# ax.set_xlabel('Predicted labels')
# ax.set_ylabel('True labels')
# ax.set_title('Confusion Matrix')
# ax.xaxis.set_ticklabels(labels)
# ax.yaxis.set_ticklabels(labels)
# plt.show()

# logistic = LogisticRegression()
# scoring = ['accuracy']
# scores = cross_validate(logistic,X_train, y_train, scoring = scoring, cv = 5, return_train_score=True, return_estimator=True, verbose = 10)
# print(scores['train_accuracy'])
# print(scores['test_accuracy'])
# print(scores['estimator'])

# for model in scores['estimator']:
#     print(model.coef_)


from sklearn.tree import DecisionTreeClassifier

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.33, random_state=324)

data = DecisionTreeClassifier(criterion='entropy', max_leaf_nodes=10, random_state=0)
data.fit(X_train, y_train)

y_predicted = data.predict(X_test)
print(y_predicted[:10])
print(y_test[:10])

print(accuracy_score(y_test, y_predicted) * 100)

print(df.iloc[-1])

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import tree
from IPython.display import SVG
from graphviz import Source
from IPython.display import display
import dtreeviz
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree


plt.figure(figsize=(8,6))

plot_tree(
    data,
    feature_names=X_train.columns,
    filled=True,
    rounded=True,
    fontsize=8
)

plt.show()

# from sklearn.tree import DecisionTreeRegressor
# data = DecisionTreeRegressor(max_depth=4, random_state=0)
# data.fit(X_train, y_train)

# plt.figure(figsize=(25,12))

# plot_tree(
#     data,
#     feature_names=independent_variable,
#     filled=True,
#     rounded=True
# )

# plt.show()
