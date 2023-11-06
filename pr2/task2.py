import pandas as pd

# Укажите полный путь к файлу
file_path = 'airports.csv'

# Загрузка данных из CSV-файла
df = pd.read_csv(file_path)

# Вывести информацию о данных
df.info()

# Вывести первые несколько строк данных
df.head()

# Проверка данных на наличие пустых значений
if df.isnull().values.any():

    # Удалить строки с пустыми значениями
    df = df.dropna()
