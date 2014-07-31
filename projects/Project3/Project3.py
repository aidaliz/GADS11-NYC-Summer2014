import pandas as pd
import numpy as np
from sklearn.ensemble.weight_boosting import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

test = pd.DataFrame.from_csv("/Users/aidalizmaldonado/GADS11-NYC-Summer2014/projects/Project3/lemon_training.csv")

#Data Pre-processing

#Change the Purchasing Date from a string to a date field type.
PurchDate = []
for date in test['PurchDate']:
	PurchDate.append(pd.Timestamp(date))
test['PurchDate'] = PurchDate
print test['PurchDate'][0:10]


#n_estimators = 30

#ABCLF = AdaBoostClassifier(DecisionTreeClassifier(test), n_estimators = n_estimators)