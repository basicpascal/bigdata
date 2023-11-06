import pandas as pd

# Укажите полный путь к файлу
file_path = 'airports.csv'

# Загрузка данных из CSV-файла
df = pd.read_csv(file_path)

# Установите опцию для отображения максимального количества строк
pd.set_option('display.max_rows', None)

print(df)
