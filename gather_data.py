import pandas as pd
import pandas_profiling
import xlrd


url = (
    'http://biostat.mc.vanderbilt.edu/'
    'wiki/pub/Main/DataSets/titanic3.xls'
)

df = pd.read_excel(url)
orig_df = df

print(df.dtypes)

# use pd.get_dummies on low cardinality categorical features

pandas_profiling.ProfileReport(df)
