"""


Author: Daniel Markusson


"""

import xgboost as xgb
from sklearn.model_selection import train_test_split
from algorithm.article_classifier.dataframe_creator import get_dataframe

articles = get_dataframe()


X, y = articles.drop('is-fake', axis=1), articles[['is-fake']]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

dtrain_reg = xgb.DMatrix(X_train, y_train, enable_categorical=True)
dtest_reg = xgb.DMatrix(X_test, y_test, enable_categorical=True)


params = {"objective": "reg:squarederror", "tree_method": "hist"}
evals = [(dtrain_reg, "train"), (dtest_reg, "validation")]

n = 10000

model = xgb.train(
    params=params,
    dtrain=dtrain_reg,
    num_boost_round=n,
    evals=evals,
    verbose_eval=10,
    early_stopping_rounds=20,

)


results = xgb.cv(
    params, dtrain_reg, num_boost_round=n, nfold=5, early_stopping_rounds=20
)

best_rmse = results['test-rmse-mean'].min()

print(best_rmse)
