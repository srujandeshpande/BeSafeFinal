import pandas
df = pandas.read_csv('rows.csv')
df = df.dropna()
#df[[0:500],:]
print(df.index)
df.to_csv('rows_c.csv')
