

## Training 3 types of data encoding


#Count Frequency Encoding
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
df = pd.read_csv(r'C:\Users\leand\OneDrive\Documentos\FormacaoDSA\f_projeto5\Scripts-05\Labs\dados\dataset.csv', usecols=['X1', 'X2', 'X3'])

print(df.head())
print(df.info())

for x in df.columns:
    # print(x,'--', len(df[x].unique()), 'categorias')
    hertz = df[x].value_counts().to_dict()
    df[x] = df[x].map(hertz)

print(df.head())
print(df.isnull().any())


