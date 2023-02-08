"""
This is a boilerplate pipeline 'split_data'
generated using Kedro 0.18.4
"""
from imblearn.over_sampling import RandomOverSampler
import pandas as pd
from sklearn import model_selection as ms


def split_data(df: pd.DataFrame) -> dict:
    X = df.drop(columns=['stroke', 'id'])
    y = df['stroke']

    ros = RandomOverSampler(random_state=42)
    X_os, y_os = ros.fit_resample(X, y)
    X_train, X_test, y_train, y_test = ms.train_test_split(X_os, y_os, test_size=0.3, random_state=42)
    return {"x_train": X_train, "x_test": X_test, "y_train": y_train, "y_test": y_test}
