from sklearn.datasets import fetch_california_housing
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Загрузка набора данных
data = fetch_california_housing(as_frame=True)

# Использовать метод info()
print("Информация о данных: ")
print(data.frame.info())

# Узнать, есть ли пропущенные значения, используя isna().sum()
print("Количество пропущенных значений в каждом признаке: ")
print(data.frame.isna().sum())

# Вывести записи, где средний возраст домов в районе более 50 лет и население более 2500 человек, используя метод loc()
filtered_data = data.frame.loc[(data.frame["AveOccup"] > 50) & (data.frame["Population"] > 2500)]
print("Записи, где средний возраст домов > 50 и население > 2500: ")
print(filtered_data)

# Узнать максимальное и минимальное значения медианной стоимости дома
max_median_house_value = data.frame["MedHouseVal"].max()
min_median_house_value = data.frame["MedHouseVal"].min()
print("Максимальная медианная стоимость дома: ", max_median_house_value)
print("Минимальная медианная стоимость дома: ", min_median_house_value)

# Используя метод apply(), вывести на экран название признака и его среднее значение
mean_values = data.frame.apply(lambda x: (x.name, x.mean()))
print("Средние значения признаков: ")
for name, mean_value in mean_values.items():
    print(name + ":", mean_value)
