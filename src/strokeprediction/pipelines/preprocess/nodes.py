"""
This is a boilerplate pipeline 'preprocess'
generated using Kedro 0.18.4
"""
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def fill_na(df: pd.DataFrame) -> pd.DataFrame:
    mean_val = df['bmi'].mean()
    df['bmi'].fillna(value=mean_val, inplace=True)
    return df


def encode_data(df: pd.DataFrame) -> pd.DataFrame:
    columns_to_encode = ['gender', 'work_type', 'ever_married', 'Residence_type', 'smoking_status']
    ohe = OneHotEncoder(handle_unknown="ignore")
    for col in columns_to_encode:
        unique_vals = df[col].unique()
        enc_df = pd.DataFrame(ohe.fit_transform(df[[col]]).toarray())
        enc_df.columns = [f'{col}_{i}' for i in range(len(unique_vals))]
        df = df.join(enc_df)
        df = df.drop([col], axis=1)
    return df
