import pandas as pd
import numpy as np

us_pop_hist = pd.read_excel('PEPANNRES_2010-2019.xlsx', sheet_name='Data')
us_pop_2020 = pd.read_excel('PEPANNRES_ESTIMATE_2020-table02.xlsx', header=3)


us_pop_hist = us_pop_hist.set_index('Geographic Area Name')
us_pop_2020 = us_pop_2020.set_index('AREA')

us_pop_hist = us_pop_hist.replace(',','', regex=True)
us_pop_2020 = us_pop_2020.rename(index={'TOTAL RESIDENT POPULATION1':'United States'})

#print(us_pop_hist.index)
#print(us_pop_2020.index)

#print(us_pop_hist.head())
#print(us_pop_2020.head())

df = us_pop_hist.join(us_pop_2020)
df = df.drop(columns=['This cell is intentionally blank.'])

print(df.head())

