"""

    Author: Daniel Markusson

"""

import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split

articles = pd.read_csv('./algorithm/article_classifier/training_set.csv')


X, y = articles.drop('is-fake', axis=1), articles[['is-fake']]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=1, test_size=0.33)

dtrain_reg = xgb.DMatrix(X_train, y_train)
dtest_reg = xgb.DMatrix(X_test, y_test)


params = {"objective": "reg:squaredlogerror",
          "tree_method": "exact", "eval_metric": "error", "max_depth": 5}
evals = [(dtrain_reg, "train"), (dtest_reg, "validation")]

n = 10000

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


best_error = results['test-error-mean'].min()

print("Cross Validation min error:", best_error)

# x = pd.DataFrame(
#     data=[[21658, 47, 10, 0.8624]], columns=['length', 'shares', 'num_authors', 'sentiment-score'])


# print(model.predict(xgb.DMatrix(x)))
