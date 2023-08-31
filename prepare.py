import numpy as np
import pandas as pd
import seaborn as sns
import wrangle as w

from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.model_selection import train_test_split


def split_data(df):

    seed = 42

    train, val_test = train_test_split(df, train_size = .7,
                                        random_state = seed)

    val, test = train_test_split(val_test, train_size = .5,
                                random_state = seed)

    return train, val, test


def r_scaler(df, features):

    rs = RobustScaler()

    rs.fit(df[features])

    df[['bedrooms_rs','bathrooms_rs','square_ft_rs','tax_value_rs','year_rs','tax_amount_rs']] = rs.transform(df[features])

    return df