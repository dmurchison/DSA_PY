import pandas as pd

df = pd.DataFrame({'A':[10,20,30,40], 'B':[15,25,35,45]})
df['C'] = df['A'] + df['B']
df['D'] = df['C'].apply(lambda x: x/2 if x>50 else x)

max_value = df['D'].max()

grouped_df = df.groupby('A')

mean_df = grouped_df.mean()
mean_df1 = grouped_df.apply(lambda x: x.mean())

print(max_value)

