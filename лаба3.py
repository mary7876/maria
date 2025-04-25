


import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# Загрузка данных Iris из sklearn
iris = load_iris()
X = iris.data  # Данные (4 признака: длина и ширина чашелистиков и лепестков)
y = iris.target  # Классы (0, 1, 2)
feature_names = iris.feature_names  # Названия признаков
target_names = iris.target_names  # Названия классов

# Индексы для отображения признаков
x_index = 0  # Индекс для длины чашелистика
y_index = 1  # Индекс для ширины чашелистика

# Названия для осей
x_label = feature_names[x_index]
y_label = feature_names[y_index]

# Цветовая схема для классов
colors = ['purple', 'yellow', 'green']

# Построение диаграммы рассеяния
plt.figure(figsize=(8, 6))  # Размер графика

for label, color in zip(range(len(target_names)), colors):
    # Условие для фильтрации данных по классам
    plt.scatter(X[y == label, x_index],
                X[y == label, y_index],
                label=target_names[label],
                color=color)

plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title("Размеры чашелистика Iris")
plt.legend(title="Класс")
plt.grid(True)  # Включение сетки
plt.show()


import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных macrodata
data = sm.datasets.macrodata.load_pandas().data

# Преобразование временного ряда (дата из года и квартала)
data['date'] = pd.to_datetime(data['year'].astype(str) + '-' + (data['quarter'] * 3).astype(int).astype(str))

# Выбор диапазона времени
data_filtered = data[(data['date'] >= '2000-01-01') & (data['date'] <= '2010-12-31')]

# Построение графиков временных рядов
plt.figure(figsize=(10, 6))
plt.plot(data_filtered['date'], data_filtered['realgdp'], label='Real GDP')
plt.plot(data_filtered['date'], data_filtered['realcons'], label='Real Consumption')
plt.plot(data_filtered['date'], data_filtered['realinv'], label='Real Investment')

# Оформление графика
plt.title("График динамики временных рядов (2000-2010)")
plt.xlabel("Дата")
plt.ylabel("Значение")
plt.legend()
plt.grid(True)
plt.show()