import pandas as pd
import numpy as np
from sklearn.cross_validation import  train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, log_loss

from sklearn.datasets import make_classification
from sklearn.metrics import confusion_matrix, precision_recall_curve, auc, roc_auc_score, roc_curve, recall_score, classification_report




data = pd.read_csv('traces_50_HW.csv', delim_whitespace=True)
data1 = pd.read_csv('model.csv')

X = data.values
y = data1.values

print(data.head)

clf = RandomForestClassifier(max_depth=20, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=0)

X_train = np.nan_to_num(X_train)
y_train = y_train.astype(int)
X_test= np.nan_to_num(X_test)


clf.fit(X_train, y_train)
prediction = clf.predict(X_test)

cnf_matrix = confusion_matrix(y_test, prediction)

print(cnf_matrix)

print(classification_report(y_test, prediction))

# acc = accuracy_score(y_test, prediction)
# rec = recall_score(y_test, prediction)

good = 0
for i in range(len(y_test)):
    if y_test[i] == prediction[i]:
        good += 1



print("Accuracy: {:.4%}".format(good/len(y_test)))
# print("Recall: {:.4%}".format())
# print("Accuracy of undersampled testing dataset", accuracy_score(y_test_undersample, y_pred_undersample))





