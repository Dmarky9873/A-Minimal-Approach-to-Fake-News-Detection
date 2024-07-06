"""

    Author: Daniel Markusson

"""

import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

import matplotlib.pyplot as plt

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
    # verbose_eval=10,
    early_stopping_rounds=50,
)

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

x = pd.DataFrame(
    data=[[21658, 47, 10, 0.8624]], columns=['length', 'shares', 'num_authors', 'sentiment-score'])


# print(model.predict(xgb.DMatrix(x)))

# """
#     Author: Daniel Markusson
# """

# import pandas as pd
# import xgboost as xgb
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.metrics import roc_curve, roc_auc_score
# from sklearn.model_selection import StratifiedKFold
# import matplotlib.pyplot as plt

# # Load the dataset
# articles = pd.read_csv(
#     './algorithm/article_classifier/model_trainer/training_set.csv')

# # Split the dataset into features and target
# X, y = articles.drop('is-fake', axis=1), articles['is-fake']

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, random_state=1, test_size=0.33)

# # Define the model
# model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')

# # Define the parameter grid
# param_grid = {
#     'n_estimators': [100, 200, 500],
#     'max_depth': [3, 5, 7],
#     'learning_rate': [0.01, 0.1, 0.2],
#     'subsample': [0.8, 1.0],
#     'colsample_bytree': [0.8, 1.0],
#     'gamma': [0, 1, 5]
# }

# # Define the cross-validation strategy
# cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)

# # Perform grid search
# grid_search = GridSearchCV(estimator=model, param_grid=param_grid,
#                            cv=cv, scoring='roc_auc', n_jobs=-1, verbose=2)
# grid_search.fit(X_train, y_train)

# # Get the best model
# best_model = grid_search.best_estimator_

# # Generate a no skill prediction (majority class)
# ns_probs = [0 for _ in range(len(y_test))]

# # Predict probabilities for the test set
# lr_probs = best_model.predict_proba(X_test)[:, 1]

# # Calculate ROC AUC scores
# ns_auc = roc_auc_score(y_test, ns_probs)
# lr_auc = roc_auc_score(y_test, lr_probs)

# # Print ROC AUC scores
# print('No Skill: ROC AUC=%.3f' % (ns_auc))
# print('XGBoost: ROC AUC=%.3f' % (lr_auc))

# # Calculate ROC curves
# ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)
# lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_probs)

# # Plot the ROC curve
# plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
# plt.plot(lr_fpr, lr_tpr, marker='.', label='XGBoost')

# # Axis labels
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')

# # Show the legend
# plt.legend()

# # Show the plot
# plt.show()

# # Test the model with a new sample
# x = pd.DataFrame(data=[[21658, 47, 10, 0.8624]], columns=[
#                  'length', 'shares', 'num_authors', 'sentiment-score'])

# # Predict the probability for the new sample
# print(best_model.predict_proba(x)[0][1])
