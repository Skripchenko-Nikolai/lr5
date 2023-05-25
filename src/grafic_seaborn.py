import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("beer.tsv", delimiter=" ")
df['id'].astype('int')
df['ame'].astype('string')
df['calories'].astype('int')
df['sodium'].astype('int')
df['alcohol_min'].astype('float')
df['alcohol_max'].astype('float')
df['cost'].astype('float')

df["avg_alcohol"] = (df["alcohol_min"] + df["alcohol_min"]) / 2

sns.pairplot(data=df, vars=["alcohol_min", "alcohol_min"])
plt.show()

sns.jointplot(data=df, x="alcohol_min", y="alcohol_min")
plt.show()

sns.violinplot(data=df, x="cost", y="avg_alcohol")
plt.show()

best_openings = df["ame"].value_counts().head(10).index
df1 = df[df["ame"].isin(best_openings)][["ame", "sodium", "cost"]]

sns.heatmap(df1.pivot_table(index="ame", columns="sodium", values="cost", aggfunc=np.mean), annot=True)
plt.show()
