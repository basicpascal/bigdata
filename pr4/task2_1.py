import numpy as np
import pandas as pd


def second_task():
    # Выгрузка данных
    data_2015 = pd.read_csv("csv/2015.csv")

    # Чтение данных
    data_2015.head()

    # Проверка на наличие пропущенных значений
    for column in data_2015.columns:
        missing = np.mean(data_2015[column].isna() * 100)
        #print(f"{column} : {round(missing, 1)}%")

    # Статистика по данным
    data_2015.describe()

    # Построение матрицы корреляции по одной целевой переменной
    corr_matrix = data_2015.corr().Happiness_Score.to_frame().round(2)
    print(corr_matrix)


second_task()
