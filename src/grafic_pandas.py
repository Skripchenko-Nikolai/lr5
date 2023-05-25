import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

df = pd.read_csv("beer.tsv", delimiter=" ")
df['id'].astype('int')
df['ame'].astype('string')
df['calories'].astype('int')
df['sodium'].astype('int')
df['alcohol_min'].astype('float')
df['alcohol_max'].astype('float')
df['cost'].astype('float')

df["avg_alcohol"] = (df["alcohol_min"] + df["alcohol_min"]) / 2

# 1.1
name = df["ame"].value_counts().head(5)
top_names = name.index
plt.bar(top_names, name)
plt.show()


# 1.2
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ax1.title.set_text('Цена больше среднего')
ax2.title.set_text('Цена меньше среднего')
ax3.title.set_text('Цена больше')
ax3.xaxis.set_label_text('Колличество натрия у большой стоимсоти')

plt.subplot(221)
sr = df.loc[(df['cost'] >= 0.4) & (df['cost'] <= 0.7)]
plt.plot(sr['cost'])

plt.subplot(222)
small = df.loc[df['cost'] < 0.4]
plt.plot(small['cost'])

plt.subplot(223)
max = df.loc[df['cost'] > 0.7]
plt.plot(max['cost'])

plt.subplot(224)
sodium_max = df[df['cost'] > 0.7].value_counts()
plt.scatter(sodium_max.index, sodium_max)

plt.show()

# 2

df[df["alc"] == True].plot(
    x="alcohol_min", y="alcohol_max", kind='scatter')
plt.show()

df["cost"].plot(kind='kde')
plt.show()

df.boxplot(column=["avg_alcohol"], by=["cost"])
plt.show()

# 5

best_openings=df["ame"].value_counts().head(15).reset_index()
fig = px.pie(best_openings, names="index",values="ame")
fig.show()
