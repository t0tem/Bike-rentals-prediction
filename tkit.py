import pandas as pd
def feat_info(df):
    info = pd.concat([pd.Series(df.dtypes, name='type'),
                      pd.Series(df.nunique(), name='n unique'),
                      pd.Series(df.isnull().sum(), name='n null'),
					  pd.Series(df.count(), name='n non-null'),
                      df.head(3).T,
                      df.tail(3).T], axis=1)
    return info