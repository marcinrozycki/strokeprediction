"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.18.4
"""
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, accuracy_score, f1_score, roc_auc_score


def train_model(splitted_data):
    X_train = splitted_data['x_train']()
    X_test = splitted_data['x_test']()
    y_train = splitted_data['y_train']()
    y_test = splitted_data['y_test']()

    lr = linear_model.LinearRegression()
    lr.fit(X_train, y_train)

    y_pred_proba = lr.predict(X_test)
    y_pred = (y_pred_proba >= 0.3).astype(np.float32)

    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(f"AUC: {roc_auc_score(y_test, y_pred_proba)}")
    print(f"Mean squared error: {mean_squared_error(y_test, y_pred_proba)}")
    print(f"F1 score: {f1_score(y_test, y_pred)}")
    return lr
