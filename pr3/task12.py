import pandas as pd

# Загрузка данных из файла
df = pd.read_csv('csv/ECDCCases.csv')

# Поиск дубликатов
duplicate_rows = df[df.duplicated()]

# Вывод информации о дубликатах, если они есть
if not duplicate_rows.empty:
    print('Найдены дубликаты данных: ')
    print(duplicate_rows)
else:
    print("Дубликатов данных не найдено")

# Удаление дубликатов
df = df.drop_duplicates()

# Проверка, что дубликаты удалены
if df.duplicated().sum() == 0:
    print('Дубликаты успешно удалены')
