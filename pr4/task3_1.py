import numpy as np
import pandas as pd
from scipy import stats


def third_task():
    # Предобработка данных
    data = pd.read_csv('csv/insurance.csv')
    data.head()
    for column in data.columns:
        missing = np.mean(data[column].isna() * 100)
        # print(f"{column} : {round(missing, 1)}%")
    data.describe()

    # Уникальные значения регионов
    data.region.unique()

    # Группируем данные индекса массы тела по региону
    frame = pd.DataFrame({'region': data['region'], 'bmi': data['bmi']})
    groups = frame.groupby('region').groups

    southwest = data['bmi'][groups['southwest']]
    southeast = data['bmi'][groups['southeast']]
    northwest = data['bmi'][groups['northwest']]
    northeast = data['bmi'][groups['northeast']]

    # Выполняем однофакторный ANOVA тест
    print(stats.f_oneway(southwest, southeast, northwest, northeast))


third_task()
