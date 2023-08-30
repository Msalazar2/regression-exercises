import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

from env import get_connection

def get_zillow():
    
    filename = 'zillow.csv'
    
    if os.path.isfile(filename):
        
        print('found data')
        
        return pd.read_csv(filename)
    
    else:
        
        print('retrieving data')
        
        query = '''
                SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
                FROM properties_2017
                WHERE propertylandusetypeid = '261';
                '''
        
        url = get_connection('zillow')
        
        df = pd.read_sql(query, url)
        
        df.to_csv(filename, index = 0)
        
        return df

def clean_zillow():
    
    df = get_zillow()
    
    df = df.rename(columns={'bedroomcnt': 'bedrooms', 'bathroomcnt': 'bathrooms', 'calculatedfinishedsquarefeet': 'square_ft', 
                            'taxvaluedollarcnt': 'tax_value', 'yearbuilt': 'year', 'taxamount': 'tax_amount'})
    
    # fill year nulls in fip with median year
    df.loc[df['fips'] == 6037, 'year'] = df.loc[df['fips'] == 6037, 'year'].fillna(1953)
    
    df.loc[df['fips'] == 6111, 'year'] = df.loc[df['fips'] == 6111, 'year'].fillna(1973)
    
    df.loc[df['fips'] == 6059, 'year'] = df.loc[df['fips'] == 6059, 'year'].fillna(1970)
    
    #fill square ft nulls in 6037 fip with median square ft
    df.loc[df['fips'] == 6037, 'square_ft'] = df.loc[df['fips'] == 6037, 'square_ft'].fillna(1535)
    
    df.loc[df['fips'] == 6059, 'square_ft'] = df.loc[df['fips'] == 6059, 'square_ft'].fillna(1831)
    
    df.loc[df['fips'] == 6111, 'square_ft'] = df.loc[df['fips'] == 6111, 'square_ft'].fillna(1811)
    
    #drop remainding nulls
    df = df.dropna()
    
    #cast to int
    df.tax_value = df.tax_value.astype('int')
    
    df.year = df.year.astype('int')
    
    df.square_ft = df.square_ft.astype('int')
    
    df.bedrooms = df.bedrooms.astype('int')
    
    
    
    #rename fips column and values
    df['fips'] = df['fips'].map({6037: 'Los Angeles', 6059: 'Orange', 6111: 'Ventura'})
    
    df = df.rename(columns = {'fips': 'county'})
    
    return df