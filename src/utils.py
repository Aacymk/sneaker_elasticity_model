import pandas as pd
import numpy as np

def log_transform(df, col):
    df[col] = np.log(df[col])
    return df

def scale_features(df, features):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    return df, scaler

def save_clean_csv(df, filename, path):
    df.to_csv(f"{path}/{filename}.csv", index=False)
