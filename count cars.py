import pandas as pd
df = pd.read_csv('/home/hanieh/car/bama.csv')
m = df.value_counts(["brand", "model"])
# print(df)
print(type(m))
m.to_csv('/home/hanieh/car/counter.csv')