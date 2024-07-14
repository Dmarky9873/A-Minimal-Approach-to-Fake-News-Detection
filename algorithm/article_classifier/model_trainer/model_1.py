"""

    Author: Daniel Markusson

"""

import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import accuracy_score


articles = pd.read_csv(
    './algorithm/article_classifier/model_trainer/training_set.csv')


X, y = articles.drop('is-fake', axis=1), articles[['is-fake']]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=1, test_size=0.33)

dtrain_reg = xgb.DMatrix(X_train, y_train)
dtest_reg = xgb.DMatrix(X_test, y_test)


params = {"objective": "binary:logistic",
          "tree_method": "exact", "max_depth": 5}
evals = [(dtrain_reg, "train"), (dtest_reg, "validation")]

n = 500

model = xgb.train(
    params=params,
    dtrain=dtrain_reg,
    num_boost_round=n,
    evals=evals,
    verbose_eval=10,
    early_stopping_rounds=50,
)


results = xgb.cv(
    params, dtrain_reg, num_boost_round=n, nfold=5, early_stopping_rounds=50, verbose_eval=10
)


mean_logloss = results['test-logloss-mean'].mean()

print("Cross Validation mean logloss:", mean_logloss)

print("Accuracy:", accuracy_score(y_test, model.predict(dtest_reg).round()))


model.save_model('./algorithm/article_classifier/model.ubj')

ns_probs = [0 for _ in range(len(y_test))]

lr_probs = model.predict(dtest_reg)

ns_auc = roc_auc_score(y_test, ns_probs)
lr_auc = roc_auc_score(y_test, lr_probs)

print('No Skill: ROC AUC=%.3f' % (ns_auc))
print('Logistic: ROC AUC=%.3f' % (lr_auc))

ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)
lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_probs)

plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
plt.plot(lr_fpr, lr_tpr, marker='.', label='Logistic')

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')

plt.legend()
plt.show()

# Confusion matrix
actual = dtest_reg.get_label()
predicted = model.predict(dtest_reg).round()
print(actual)
print(predicted)

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix, display_labels=[0, 1])

cm_display.plot()
plt.show()
