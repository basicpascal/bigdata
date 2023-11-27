import numpy as np
import pandas as pd


def third_task():
    # Предобработка данных
    data = pd.read_csv('csv/insurance.csv')
    data.head()
    for column in data.columns:
        missing = np.mean(data[column].isna() * 100)
        #print(f"{column} : {round(missing, 1)}%")
    data.describe()

    # Уникальные значения регионов
    print(data.region.unique())


third_task()
