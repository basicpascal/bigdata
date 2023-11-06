import pandas as pd

# Загрузить данные из файла
df = pd.read_csv('csv/ECDCCases.csv')

# Проверить наличие пропущенных значений и вывести количество в процентах
missing_percentage = df.isnull().mean()*100

# Найти два признака с наибольшим количеством пропусков
columns_to_drop = missing_percentage.nlargest(2).index

# Удалить эти признаки
df.drop(columns=columns_to_drop,inplace=True)

# Заполнить пропуски в оставшихся категориальных признаках значениеи "Other"
categorical_columns = df.select_dtypes(include=['object']).columns
df[categorical_columns] = df[categorical_columns].fillna('other')

# Заполнить пропуски в оставшихся числовых признаках медианным значением
numeric_columns = df.select_dtypes(include=['number']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())

# Проверить, что больше нет пропусков в данных нет
missing_percentage_after = df.isnull().mean()*100

print('Процент пропущенных значений после обработки: ')
print(missing_percentage_after)
