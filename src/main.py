import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt


df = pd.read_csv("beer.tsv", delimiter=" ")
df['id'].astype('int')
df['ame'].astype('string')
df['calories'].astype('int')
df['sodium'].astype('int')
df['alcohol_min'].astype('float')
df['alcohol_max'].astype('float')
df['cost'].astype('float')

print("\n2.2 вывод первых 5 элементов таблицы")
print(df.head(5))

print("\n2.3 вывод последних 5 элементов таблицы")
print(df.tail(5))

print("\n2.4 использовать функцию describe()")
print(df.describe(include=[np.number])["cost"])

print("\n2.5 считывание значения конкретной ячейки")
print(df["cost"].values[3])
print(df.at[3, 'cost'])
print(df.loc[3]['cost'])

print("\n2.6 фильтрация строк по диапазону индекса")
print(df.filter(items=range(5, 10), axis=0))

print("\n2.7 фильтрация набора данных по какому-либо условию")
print(df[df["calories"] > 150])

print("\n2.8 работа с пропущенными значениями")
df.iloc[1, 6] = np.nan
print("has empty columns:{}".format(df.isnull().values.any()))
print("remsolving empty values")
for i in df.columns[df.isnull().any(axis=0)]:  # ---Applying Only on variables with NaN values
    df[i].fillna(df[i].mean(), inplace=True)
print("has empty columns:{}".format(df.isnull().values.any()))

print("\n2.9 создание нового поля вычисленного на основе значений других полей")

print("\n2.9.1 через выражение на базе имеющихся колонок")
df["avg_alcohol"] = (df["alcohol_min"] + df["alcohol_max"]) / 2
print(df["avg_alcohol"])

print("\n2.9.2 через DataFrame.apply")
df["avg_alcohol_apply"] = df.apply(lambda row: (row.alcohol_min + row.alcohol_max) / 2, axis=1)
print(df["avg_alcohol_apply"])

print("\n2.9.3 через Series.apply")
df["name_normal"] = df["ame"].apply(lambda ame: ame.split("_")[0])
print(df["name_normal"])

print("\n2.10 сортировка по какому-либо из полей")
df.sort_values(by=["avg_alcohol"], ignore_index=True, inplace=True)
print(df["avg_alcohol"])

print("\n2.11 вычислить несколько статистик по колонкам")
print("Средней стоимости")
srDf = df.loc[(df['cost'] >= 0.4) & (df['cost'] <= 0.7)]
print(srDf)

print("\n2.12 .value_counts()")
print("openings count:{}".format(df["name_normal"].value_counts()))

print("\n2.13 Вывод уникальных значений колонки")
print("Уникальных id")
print(df["id"].unique())

print("\n2.14 Удалите текущий индекс и создайте новый индекс на базе новой колонки")
df.reset_index(drop=True, inplace=True)
df.set_index('id', inplace=True)
print(df)
