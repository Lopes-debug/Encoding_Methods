

## Training 3 types of data encoding


#Count Frequency Encoding
# import pandas as pd
# import numpy as np
# pd.set_option('display.max_columns', None)
# df = pd.read_csv(r'C:\Users\leand\OneDrive\Documentos\FormacaoDSA\f_projeto5\Scripts-05\Labs\dados\dataset.csv', usecols=['X1', 'X2', 'X3'])

# print(df.head())
# print(df.info())

# for x in df.columns:
#     # print(x,'--', len(df[x].unique()), 'categorias')
#     hertz = df[x].value_counts().to_dict()
#     df[x] = df[x].map(hertz)

# print(df.head())
# print(df.isnull().any())


#Label Encoding
import pandas as pd
import datetime as dt

data_ = dt.datetime.now()
# print(data_)
data_list = [data_ - dt.timedelta(days=x) for x in range(0,20)]
df = pd.DataFrame(data_list)
# print(df.head())
df.columns = ['data']
df['days_week'] = df['data'].dt.day_name()
dict_days_week = {
    'Monday':1,
    'Tuesday':2,
    'Wednesday':3,
    'Thursday':4,
    'Friday':5,
    'Saturday':6,
    'Sunday':7
    }

df['days_week_cod'] = df['days_week'].map(dict_days_week)
print(df)