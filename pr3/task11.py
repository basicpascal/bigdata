import pandas as pd

# Загрузка данных из файла
df = pd.read_csv('csv/ECDCCases.csv')

# Посмотреть статистику по данным, используя describe()
data_description = df.describe()

# Вывести статистику
print(data_description)

# Определить выбросы с помощью межквартильного размаха (IQR)
Q1 = df['deaths'].quantile(0.25)
Q3 = df['deaths'].quantile(0.75)
IQR = Q3 - Q1

# Определить границы выбросов
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Найти выбросы в признаке 'Deaths'
outliers = df[(df['deaths'] < lower_bound) | (df['deaths'] > upper_bound)]

# Вывести информацию о выбросах
print("Выбросы в признаке 'Deaths': ")
print(outliers)

# Определить страны, в которых количество смертей в день превысило 3000
high_deaths = df[df['deaths'] > 3000]

# Вывести информацию о странах с высоким количеством смертей
print(f'Страны, в которых количество смертей в день превысило 3000: ')
print(high_deaths[['countriesAndTerritories', 'deaths']])

# Посчитать количество таких дней
count_high_deaths_days = len(high_deaths)
print(f'Количество дней с количеством смертей в день более 3000: {count_high_deaths_days}')
