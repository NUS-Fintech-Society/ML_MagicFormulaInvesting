import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score
from sklearn.model_selection import GridSearchCV
train = pd.read_csv('Training_Data.csv')
test = pd.read_csv('Test_Data.csv')
clf = SVC()
param_grid = {'C': [0.001,0.01,0.1,1,10,100,1000,10000], 
              'gamma': [1000,10000,20000,40000,50000,60000,70000,100000],'kernel': ['rbf']}
grid = GridSearchCV(clf, param_grid = param_grid,refit=True,verbose=2)
grid.fit(train[['roc','ey']], train['label'])
label_pred = grid.predict(test[['roc','ey']])
print(classification_report(label_pred, test['label']))
print(confusion_matrix(label_pred, test['label']))
print(accuracy_score(label_pred,test['label']))
print(precision_score(label_pred,test['label']))
print(grid.best_params_)
'''
              precision    recall  f1-score   support

           0       1.00      0.83      0.91       228
           1       0.49      1.00      0.66        37

    accuracy                           0.86       265
   macro avg       0.75      0.92      0.78       265
weighted avg       0.93      0.86      0.87       265

[[190  38]
 [  0  37]]
0.8566037735849057
0.49333333333333335
{'C': 1, 'gamma': 40000, 'kernel': 'rbf'}
'''