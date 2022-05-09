
# Functions

import pandas as pd
import numpy as np

def standarizate_cols (df):
    
    '''
    Standarizes column names
    - Sets cols to lowercase.
    - Replaces empty space for '_'.
    
    Args:
        df: The dataframe to be standarized.
        
    Returns:
        A df that has been standarized.
    '''
    
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df


def nulls_percent (df):
    
    '''
    Shows percent of nulls in a data frame.
    
    Args:
        df: The dataframe we want to check out.
        
    Returns:
        A new df with 2columns:
        - 'column_name' with the name of the original df columns
        - 'nulls_percentage' with the percentage of nulls in every column
    '''
    nulls_percent = pd.DataFrame(df.isna().sum()/len(df)).reset_index()
    nulls_percent.columns = ['column_name', 'nulls_percentage']
    
    return nulls_percent