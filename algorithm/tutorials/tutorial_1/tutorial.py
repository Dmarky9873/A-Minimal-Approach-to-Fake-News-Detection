from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the data
dataset = loadtxt(
    '/Users/danielmarkusson/Documents/GitHub/Analyzing-the-Spread-of-Online-Media/algorithm/tutorial/pima-indians-diabetes.csv', delimiter=",")

# Split data into X and Y
X = dataset[:, 0:8]
Y = dataset[:, 8]

# Split the data into train and test sets
seed = 1
test_size = 0.33
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
