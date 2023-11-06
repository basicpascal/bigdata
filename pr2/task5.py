import pandas as pd
import matplotlib.pyplot as plt

# Укажите полный путь к файлу на диске D:
file_path = 'airports.csv'

# Загрузка данных из CSV-файла
df = pd.read_csv(file_path)

df = df.head(15)

# Выберите параметр для анализа (например, "latitude_deg")
parameter = "latitude_deg"

# Выберите несколько показателей для сравнения (от 2 до 5)
indicators = ["longitude_deg"]

# Создайте новый график
plt.figure(figsize=(10, 6))

# Для каждого показателя построить линейный график
for indicator in indicators:
    plt.plot(df[parameter], df[indicator], marker='o', color='crimson', markersize=8, markerfacecolor='white', markeredgecolor='black', markeredgewidth=2, label=indicator)

# Настройте название графика и осей
plt.title(f"Зависимость {parameter} от {', '.join(indicators)}")
plt.xlabel(parameter)
plt.ylabel("Значения показателей")

# Добавьте легенду
plt.legend()

# Включите сетку
plt.grid(linewidth=2, color='mistyrose')

# Отобразите график
plt.show()
