from scipy import stats
import pandas as pd


#function that changes churn values to Yes & No, and drops insignificant columns to return x and y split
def xy_split(df):
    
    return df.drop(columns= 'tax_value'), df.tax_value
    

#function applies one hot encoding to categorical feature and drops repetitave features
def dummies(df, df2):
    
    df = pd.get_dummies(df)
    
    df2 = pd.get_dummies(df2)
    
    return df, df2