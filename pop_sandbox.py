import pandas as pd
import numpy as np

us_pop_hist = pd.read_excel('PEPANNRES_2010-2019.xlsx', sheet_name='Data')
us_pop_2020 = pd.read_excel('PEPANNRES_ESTIMATE_2020-table02.xlsx', header=3)


us_pop_hist = us_pop_hist.set_index('Geographic Area Name')
us_pop_2020 = us_pop_2020.set_index('AREA')

us_pop_hist = us_pop_hist.replace(',','', regex=True)
us_pop_hist = us_pop_hist.apply(pd.to_numeric)
us_pop_2020 = us_pop_2020.rename(index={'TOTAL RESIDENT POPULATION1':'United States'})
us_pop_2020 = us_pop_2020.apply(pd.to_numeric)

#print(us_pop_hist.index)
#print(us_pop_2020.index)

#print(us_pop_hist.head())
#print(us_pop_2020.head())

df = us_pop_hist.join(us_pop_2020)
df = df.drop(columns=['This cell is intentionally blank.'])

#df['RESIDENT POPULATION (APRIL 1, 2020)'] = pd.to_numeric(df['RESIDENT POPULATION (APRIL 1, 2020)'])

df['10Y Change Amount'] = df['RESIDENT POPULATION (APRIL 1, 2020)']-df['4/1/2010 Census population']
df['10Y Change %'] = df['10Y Change Amount']/df['4/1/2010 Census population']

#df_change = df.sort_values(by=['10Y Change %'], ascending=False)

df['1Y Prior %'] = (df['RESIDENT POPULATION (APRIL 1, 2020)']-df['7/1/2019 population estimate'])/df['7/1/2019 population estimate']

df_1y_change = df.sort_values(by=['1Y Prior %'], ascending=False)
#print(df_1y_change.head(25))

df['2Y Prior %'] = (df['RESIDENT POPULATION (APRIL 1, 2020)']-df['7/1/2018 population estimate'])/df['7/1/2018 population estimate']

df_2y_change = df.sort_values(by=['2Y Prior %'], ascending=False)
#print(df_2y_change.head(25))

#print(df_change.head(35))

df['3Y Prior %'] = (df['RESIDENT POPULATION (APRIL 1, 2020)']-df['7/1/2017 population estimate'])/df['7/1/2018 population estimate']

df_3y_change = df.sort_values(by=['3Y Prior %'], ascending=False)
print(df_3y_change.head(25))


