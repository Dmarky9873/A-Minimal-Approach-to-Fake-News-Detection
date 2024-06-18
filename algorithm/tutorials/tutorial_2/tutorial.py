"""

    Courtesy of: https://www.datacamp.com/tutorial/xgboost-in-python

"""

import xgboost as xgb
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split


diamonds = sns.load_dataset("diamonds")
print(diamonds.head())

X, y = diamonds.drop('price', axis=1), diamonds[['price']]

cats = X.select_dtypes(exclude=np.number).columns.tolist()

for col in cats:
    X[col] = X[col].astype('category')

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# Create regression matrices
dtrain_reg = xgb.DMatrix(X_train, y_train, enable_categorical=True)
dtest_reg = xgb.DMatrix(X_test, y_test, enable_categorical=True)


# Define hyperparameters
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
