import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


def second_task():
    # Выгрузка данных
    data_2015 = pd.read_csv("csv/2015.csv")

    # Чтение данных
    data_2015.head()

    # Проверка на наличие пропущенных значений
    for column in data_2015.columns:
        missing = np.mean(data_2015[column].isna() * 100)
        # print(f"{column} : {round(missing, 1)}%")

    # Статистика по данным
    data_2015.describe()

    # Построение матрицы корреляции по одной целевой переменной
    corr_matrix = data_2015.corr().Happiness_Score.to_frame().round(2)
    # print(corr_matrix)

    # Модель LinearRegression
    model = LinearRegression()

    # Переменные для модели
    x = data_2015[['Economy (GDP per Capita)']]
    y = data_2015['Happiness_Score']
    x = np.array(x, type(float))
    y = np.array(y, type(float))

    # Коэффициенты сдвига и наклона
    model.fit(x, y)
    # print(model.coef_, model.intercept_)

    # Построение модели с линией регрессии
    model_a = model.coef_[0]
    model_b = model.intercept_

    model_y_sk = model_a * x + model_b

    fig = plt.figure(figsize=(10, 6))
    plt.plot(x, model_y_sk, linewidth=2, color='r', label=f'linear_model = {model_a:.2f}x + {model_b:.2f}')
    plt.scatter(x, y, alpha=0.7)
    plt.grid()
    plt.xlabel('Economy (GDP per Capita)')
    plt.ylabel('Happiness Score')
    plt.legend(prop={'size': 16})
    plt.show()


second_task()
