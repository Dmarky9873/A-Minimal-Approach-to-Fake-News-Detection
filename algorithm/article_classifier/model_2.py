"""


Author: Daniel Markusson


"""

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

articles = pd.read_csv('./algorithm/article_classifier/training_set.csv')

X, Y = articles.drop('is-fake', axis=1), articles[['is-fake']]

# Split the data into train and test sets
seed = 2
test_size = 0.60
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=test_size, random_state=seed)

# Fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)

# Make predictions for test data

y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]

# Evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

print(y_test['is-fake'].to_list())
print(predictions)
